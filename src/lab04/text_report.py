import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Отсортировать (слово, частота): count ↓, затем слово ↑."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", default="data/input.txt")
    parser.add_argument("--out", dest="out", default="data/report.csv")
    parser.add_argument("--encoding", default="utf-8")
    args = parser.parse_args()

    try:
        text = read_text(args.inp, encoding=args.encoding)
    except FileNotFoundError:
        print(f"Файл не найден: {args.inp}", file=sys.stderr)
        return 1
    except UnicodeDecodeError:
        print(
            f"Не удалось декодировать {args.inp} в {args.encoding!r}; "
            f"попробуйте --encoding cp1251",
            file=sys.stderr,
        )
        return 1

    freq = count_freq(tokenize(normalize(text)))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_csv(sorted_word_counts(freq), out, header=("word", "count"))

    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, cnt in (top_n(freq, 5) if freq else []):
        print(f"{word}:{cnt}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
