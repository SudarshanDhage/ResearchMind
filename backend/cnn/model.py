import torch
import torch.nn as nn
import torch.nn.functional as F


class TextCNN(nn.Module):
    """Kim-style TextCNN for binary source-quality classification.

    Convolution over word embeddings captures local n-gram patterns
    (clickbait phrases vs academic phrasing) that a plain API call does not.
    """

    def __init__(
        self,
        vocab_size: int,
        embed_dim: int = 64,
        num_classes: int = 2,
        kernel_sizes: tuple[int, ...] = (3, 4, 5),
        num_filters: int = 64,
        dropout: float = 0.5,
        pad_idx: int = 0,
    ):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_idx)
        self.convs = nn.ModuleList(
            [nn.Conv1d(embed_dim, num_filters, kernel_size=k) for k in kernel_sizes]
        )
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(num_filters * len(kernel_sizes), num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (batch, seq_len)
        embedded = self.embedding(x).transpose(1, 2)  # (batch, embed, seq)
        pooled = []
        for conv in self.convs:
            conv_out = F.relu(conv(embedded))
            pooled.append(F.max_pool1d(conv_out, kernel_size=conv_out.size(2)).squeeze(2))
        cat = self.dropout(torch.cat(pooled, dim=1))
        return self.fc(cat)
