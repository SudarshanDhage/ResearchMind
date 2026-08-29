import re
from collections import Counter

PAD, UNK = "<pad>", "<unk>"
TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


class Vocab:
    def __init__(self, word_to_id: dict[str, int] | None = None):
        self.word_to_id = word_to_id or {PAD: 0, UNK: 1}

    def __len__(self) -> int:
        return len(self.word_to_id)

    def encode(self, text: str, max_len: int) -> list[int]:
        ids = [self.word_to_id.get(tok, 1) for tok in tokenize(text)][:max_len]
        if len(ids) < max_len:
            ids = ids + [0] * (max_len - len(ids))
        return ids

    @classmethod
    def build(cls, texts: list[str], min_freq: int = 1) -> "Vocab":
        counts = Counter()
        for text in texts:
            counts.update(tokenize(text))
        word_to_id = {PAD: 0, UNK: 1}
        for word, freq in counts.most_common():
            if freq >= min_freq and word not in word_to_id:
                word_to_id[word] = len(word_to_id)
        return cls(word_to_id)
