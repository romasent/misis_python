import sys
import os
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='cp866') # фикс кодировки для Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # раскодировка для функций

sys.path.insert(0, LIB_DIR)

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
