# misis_python
# Лабораторная работа 3

## Задание 1
### `normalize`
#### Входные данные:
"ПрИвЕт\nМИр\t" → "привет мир" (casefold + схлопнуть пробелы)

"ёжик, Ёлка" (yo2e=True) → "ежик, елка"

"Hello\r\nWorld" → "hello world"

"  двойные   пробелы  " → "двойные пробелы"

![](../../images/lab03/img01.png)

## Задание 2
### `tokenize`
#### Входные данные:

"привет мир" → ["привет", "мир"]

"hello,world!!!" → ["hello", "world"]

"по-настоящему круто" → ["по-настоящему", "круто"]

"2025 год" → ["2025", "год"]

"emoji 😀 не слово" → ["emoji", "не", "слово"] (эмодзи выпадают)

![](../../images/lab03/img02.png)
## Задание 3
### `count_freq | top_n`
#### Входные данные:
Токены ["a","b","a","c","b","a"] → частоты {"a":3,"b":2,"c":1};
top_n(..., n=2) → [("a",3), ("b",2)]

При равенстве частот: токены ["bb","aa","bb","aa","cc"] → частоты {"aa":2,"bb":2,"cc":1};

top_n(..., n=2) → [("aa",2), ("bb",2)] (алфавитная сортировка при равенстве).

![](../../images/lab03/img03.png)
# КОД
```python
# ЛР3: normalize, tokenize, count_freq, top_n
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = " ".join(text.strip().split())
    if casefold:
        text = text.casefold()
    return text

# Тест кейсы normalize

#print(normalize('ПрИвЕт\nМИр\t'))
#print(normalize('ёжик, Ёлка'))
#print(normalize('Hello\r\nWorld'))
#print(normalize('  двойные   пробелы  '))

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

# Тест кейсы tokenize

print(tokenize('привет мир'))
print(tokenize('hello,world!!!'))
print(tokenize('по-настоящему круто'))
print(tokenize('2025 год'))
print(tokenize('emoji 😀 не слово'))

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word,0) + 1
    return freq                           

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0])) # сортировка по ключу
    return items[:n]

# Тест кейсы count_freq и top_n
print(top_n(count_freq(["a","b","a","c","b","a"]), n = 2))
print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n = 2))

# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]

```
