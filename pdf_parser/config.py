from dataclasses import dataclass

from constants import (
    books_OT, book_names_OT,
    books_NT, book_names_NT,
)

@dataclass(frozen=True)
class ParseConfig:
    books: dict[str, int]
    book_names: dict[str, str]
    pdf_subdir: str
    colors: set[tuple[int, int, int]] 
    
CONFIGS = {
    ("OT", "ches"): ParseConfig(
        books=books_OT,
        book_names=book_names_OT,
        pdf_subdir="OT",
        colors={(0, 128, 0), (128, 192, 128)},
    ),
    ("NT", "clis"): ParseConfig(
        books=books_NT,
        book_names=book_names_NT,
        pdf_subdir="NT",
        colors={(0, 128, 0), (128, 192, 128)},
    ),
    ("NT", "cles"): ParseConfig(
        books=books_NT,
        book_names=book_names_NT,
        pdf_subdir="NT",
        colors={(0, 128, 0), (0, 128, 128)},
    ),
}


def resolve_config(testament: str, mode: str) -> ParseConfig:
    try:
        return CONFIGS[(testament, mode)]
    except KeyError:
        raise ValueError(f"Unsupported combination: {testament} + {mode}")
