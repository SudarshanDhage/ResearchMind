"""Train the local TextCNN source-quality classifier.

This is the original ML module of the project (not an API).
Run from backend/:  python -m cnn.train
"""

from __future__ import annotations

import json
import random
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from cnn.dataset import labeled_examples
from cnn.model import TextCNN
from cnn.vocab import Vocab

CHECKPOINT_DIR = Path(__file__).resolve().parent / "checkpoints"
MAX_LEN = 80
SEED = 42


def set_seed(seed: int = SEED) -> None:
    random.seed(seed)
    torch.manual_seed(seed)


def split_data(rows: list[tuple[str, int]], val_ratio: float = 0.2):
    random.shuffle(rows)
    n_val = max(1, int(len(rows) * val_ratio))
    return rows[n_val:], rows[:n_val]


def tensors(rows: list[tuple[str, int]], vocab: Vocab):
    x = torch.tensor([vocab.encode(text, MAX_LEN) for text, _ in rows], dtype=torch.long)
    y = torch.tensor([label for _, label in rows], dtype=torch.long)
    return x, y


def accuracy(logits: torch.Tensor, y: torch.Tensor) -> float:
    pred = logits.argmax(dim=1)
    return (pred == y).float().mean().item()


def main() -> None:
    set_seed()
    rows = labeled_examples()
    train_rows, val_rows = split_data(rows)
    vocab = Vocab.build([text for text, _ in train_rows])

    train_x, train_y = tensors(train_rows, vocab)
    val_x, val_y = tensors(val_rows, vocab)
    loader = DataLoader(TensorDataset(train_x, train_y), batch_size=16, shuffle=True)

    model = TextCNN(vocab_size=len(vocab))
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()

    best_val = 0.0
    best_state = None
    for epoch in range(1, 16):
        model.train()
        total_loss = 0.0
        for xb, yb in loader:
            opt.zero_grad()
            logits = model(xb)
            loss = loss_fn(logits, yb)
            loss.backward()
            opt.step()
            total_loss += loss.item() * len(xb)

        model.eval()
        with torch.no_grad():
            train_acc = accuracy(model(train_x), train_y)
            val_acc = accuracy(model(val_x), val_y)
        print(
            f"epoch {epoch:02d}  loss={total_loss / len(train_x):.4f}  "
            f"train_acc={train_acc:.3f}  val_acc={val_acc:.3f}"
        )
        if val_acc >= best_val:
            best_val = val_acc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "model_state": best_state,
        "word_to_id": vocab.word_to_id,
        "max_len": MAX_LEN,
        "val_acc": best_val,
        "n_train": len(train_rows),
        "n_val": len(val_rows),
    }
    torch.save(payload, CHECKPOINT_DIR / "textcnn.pt")
    meta = {
        "val_acc": round(best_val, 4),
        "n_train": len(train_rows),
        "n_val": len(val_rows),
        "vocab_size": len(vocab),
        "max_len": MAX_LEN,
        "classes": {"0": "unreliable", "1": "reliable"},
    }
    (CHECKPOINT_DIR / "metrics.json").write_text(json.dumps(meta, indent=2))
    print(f"saved {CHECKPOINT_DIR / 'textcnn.pt'}  best_val_acc={best_val:.3f}")


if __name__ == "__main__":
    main()
