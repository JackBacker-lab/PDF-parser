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


def resolve_config(testament: str, mode: str) -> ParseConfig:
    if testament == "OT":
        books = books_OT
        names = book_names_OT
        pdf_subdir = "OT"
    else:
        books = books_NT
        names = book_names_NT
        pdf_subdir = "NT"

    if mode in {"ches", "clis"}:
        colors = {(0, 128, 0), (128, 192, 128)}
    elif mode == "cles":
        colors = {(0, 128, 0), (0, 128, 128)}
    else:
        raise ValueError("Unsupported mode")

    return ParseConfig(
        books=books,
        book_names=names,
        pdf_subdir=pdf_subdir,
        colors=colors,
    )
