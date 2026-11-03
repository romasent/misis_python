import argparse
import sys
import re
from pathlib import Path
from collections import Counter

def word_frequencies(text: str) -> dict[str, int]:
    """
    Считает частоту слов в тексте.
    (Заменяет функцию из lab03, так как там был только скрипт main)
    """
    # Ищем слова (буквы русского и английского алфавита)
    words = re.findall(r"[A-Za-zА-Яа-яЁё]+", text.lower())
    return dict(Counter(words))


def cmd_cat(args: argparse.Namespace) -> int:
    """Вывести файл построчно, с опцией нумерации строк."""
    path = Path(args.input)
    if not path.exists():
        print(f"Ошибка: файл не найден: {path}", file=sys.stderr)
        return 1

    try:
        with path.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                line = line.rstrip("\n")
                if args.number:
                    print(f"{i:6d}\t{line}")
                else:
                    print(line)
    except UnicodeDecodeError:
        print(f"Ошибка: файл не является текстовым: {path}", file=sys.stderr)
        return 1
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    """Вывести топ-N самых частых слов."""
    path = Path(args.input)
    if not path.exists():
        print(f"Ошибка: файл не найден: {path}", file=sys.stderr)
        return 1

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Ошибка: файл не является текстовым: {path}", file=sys.stderr)
        return 1

    freqs = word_frequencies(text)
    if not freqs:
        print("В файле не найдено слов.")
        return 0

    # Сортируем: сначала по частоте (убывание), потом по алфавиту
    sorted_items = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
    top = sorted_items[: args.top]

    print(f"Топ-{args.top} слов (файл: {path}):")
    print(f"{'Слово':<20}{'Частота':>10}")
    print("-" * 30)
    for word, count in top:
        print(f"{word:<20}{count:>10}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="cli_text",
        description="CLI-утилиты для работы с текстом: cat и stats.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- подкоманда cat ---
    cat_p = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_p.add_argument("--input", required=True, help="Путь к текстовому файлу")
    cat_p.add_argument("-n", "--number", action="store_true", help="Нумеровать строки")
    cat_p.set_defaults(func=cmd_cat)

    # --- подкоманда stats ---
    stats_p = subparsers.add_parser("stats", help="Анализ частот слов")
    stats_p.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_p.add_argument("--top", type=int, default=5, help="Сколько топ-слов вывести (по умолчанию 5)")
    stats_p.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
