"""Inference wrapper: score scraped text as reliable or unreliable."""

from __future__ import annotations

from pathlib import Path

import torch
import torch.nn.functional as F

from cnn.model import TextCNN
from cnn.vocab import Vocab

CHECKPOINT = Path(__file__).resolve().parent / "checkpoints" / "textcnn.pt"
LABELS = {0: "unreliable", 1: "reliable"}

_bundle = None


def _load():
    global _bundle
    if _bundle is not None:
        return _bundle
    if not CHECKPOINT.exists():
        raise RuntimeError(
            "CNN checkpoint missing. From backend/ run: python -m cnn.train"
        )
    payload = torch.load(CHECKPOINT, map_location="cpu", weights_only=False)
    vocab = Vocab(payload["word_to_id"])
    model = TextCNN(vocab_size=len(vocab))
    model.load_state_dict(payload["model_state"])
    model.eval()
    _bundle = (model, vocab, int(payload["max_len"]))
    return _bundle


def score_text(text: str) -> dict:
    """Return label, confidence, and whether the writer should trust this source."""
    model, vocab, max_len = _load()
    ids = torch.tensor([vocab.encode(text or "", max_len)], dtype=torch.long)
    with torch.no_grad():
        logits = model(ids)
        probs = F.softmax(logits, dim=1)[0]
    unreliable_p = float(probs[0])
    reliable_p = float(probs[1])
    label_id = int(probs.argmax().item())
    return {
        "label": LABELS[label_id],
        "reliable_score": round(reliable_p, 4),
        "unreliable_score": round(unreliable_p, 4),
        "accepted": label_id == 1 and reliable_p >= 0.55,
    }


def filter_for_writer(topic: str, search: str, reader: str) -> tuple[str, dict]:
    """Keep only CNN-accepted text for the writer. Always return a CNN report."""
    chunks = []
    if search.strip():
        chunks.append(("search", search))
    if reader.strip():
        chunks.append(("reader", reader))

    accepted_parts = []
    details = []
    for name, text in chunks:
        result = score_text(text)
        result["source"] = name
        details.append(result)
        if result["accepted"]:
            accepted_parts.append(f"{name.upper()} (CNN accepted):\n{text}")

    cnn = {
        "verdict": "accepted" if accepted_parts else "rejected",
        "details": details,
        "summary": _summary(details, accepted_parts),
    }
    if accepted_parts:
        filtered = (
            f"CNN SOURCE FILTER: only passages scored as reliable are included.\n\n"
            + "\n\n".join(accepted_parts)
        )
    else:
        filtered = (
            f"CNN SOURCE FILTER: no passage scored as reliable. "
            f"Writer must be extra cautious and state uncertainty.\n\n"
            f"TOPIC: {topic}\n\nSEARCH:\n{search[:1500]}\n\nREADER:\n{reader[:1500]}"
        )
    return filtered, cnn


def _summary(details: list[dict], accepted_parts: list[str]) -> str:
    lines = ["TextCNN source-quality scores (local model, not an API):"]
    for item in details:
        mark = "ACCEPT" if item["accepted"] else "REJECT"
        lines.append(
            f"- {item['source']}: {item['label']} "
            f"(reliable={item['reliable_score']:.2f}) → {mark}"
        )
    if accepted_parts:
        lines.append("Writer will use only CNN-accepted text.")
    else:
        lines.append("Writer is warned that sources look unreliable.")
    return "\n".join(lines)
