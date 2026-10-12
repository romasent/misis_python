import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib")) # добавляем папку lib в sys.path для запуска в консоли

from text import normalize, tokenize, count_freq, top_n

def main() -> None:
    text = sys.stdin.read()
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
