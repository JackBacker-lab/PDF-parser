import argparse
from pathlib import Path

from parser import parse
from config import ParseConfig, resolve_config

BASE_DIR = Path(__file__).resolve().parent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PDF Bible text parser (colored text extraction)")

    parser.add_argument(
        "--testament",
        choices=["OT", "NT"],
        required=True,
        help="Choose testament: OT or NT"
    )

    parser.add_argument(
        "--mode",
        choices=["ches", "clis", "cles"],
        required=True,
        help="Parsing mode / translation variant"
    )

    parser.add_argument(
        "--input",
        type=Path,
        default=BASE_DIR / "pdf_files",
        help="Directory with PDF files"
    )

    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output text file"
    )

    return parser


def main():
    args = build_parser().parse_args()
    cfg: ParseConfig = resolve_config(args.testament, args.mode)

    parse(
        books=cfg.books,
        book_names=cfg.book_names,
        dir_path=args.input / cfg.pdf_subdir,
        output_path=args.output,
        target_colors=cfg.colors
    )


if __name__ == "__main__":
    main()
