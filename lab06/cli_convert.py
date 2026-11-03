import argparse
import sys
from pathlib import Path

# Импорт функций из ЛР5. Подставьте свои реальные пути/имена.
try:
    from src.lab05.json_csv import json_to_csv, csv_to_json
    from src.lab05.csv_xlsx import csv_to_xlsx
except ImportError:
    # Заглушки для локальной проверки CLI (удалите в финальной версии)
    def json_to_csv(src, dst): Path(dst).write_text("id,name\n", encoding="utf-8")
    def csv_to_json(src, dst): Path(dst).write_text("[]", encoding="utf-8")
    def csv_to_xlsx(src, dst): Path(dst).write_text("(xlsx)", encoding="utf-8")


def _check_input(path: Path) -> bool:
    if not path.exists():
        print(f"Ошибка: входной файл не найден: {path}", file=sys.stderr)
        return False
    return True


def _ensure_out_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def cmd_json2csv(args: argparse.Namespace) -> int:
    inp, out = Path(args.input), Path(args.output)
    if not _check_input(inp):
        return 1
    _ensure_out_dir(out)
    try:
        json_to_csv(str(inp), str(out))
    except Exception as e:
        print(f"Ошибка конвертации json2csv: {e}", file=sys.stderr)
        return 1
    print(f"OK: {inp} -> {out}")
    return 0


def cmd_csv2json(args: argparse.Namespace) -> int:
    inp, out = Path(args.input), Path(args.output)
    if not _check_input(inp):
        return 1
    _ensure_out_dir(out)
    try:
        csv_to_json(str(inp), str(out))
    except Exception as e:
        print(f"Ошибка конвертации csv2json: {e}", file=sys.stderr)
        return 1
    print(f"OK: {inp} -> {out}")
    return 0


def cmd_csv2xlsx(args: argparse.Namespace) -> int:
    inp, out = Path(args.input), Path(args.output)
    if not _check_input(inp):
        return 1
    _ensure_out_dir(out)
    try:
        csv_to_xlsx(str(inp), str(out))
    except Exception as e:
        print(f"Ошибка конвертации csv2xlsx: {e}", file=sys.stderr)
        return 1
    print(f"OK: {inp} -> {out}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="cli_convert",
        description="CLI-конвертеры: json2csv, csv2json, csv2xlsx.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    for name, func, desc in [
        ("json2csv", cmd_json2csv, "JSON -> CSV"),
        ("csv2json", cmd_csv2json, "CSV -> JSON"),
        ("csv2xlsx", cmd_csv2xlsx, "CSV -> XLSX"),
    ]:
        p = sub.add_parser(name, help=desc)
        p.add_argument("--in", dest="input", required=True,
                       help="Входной файл")
        p.add_argument("--out", dest="output", required=True,
                       help="Выходной файл")
        p.set_defaults(func=func)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
