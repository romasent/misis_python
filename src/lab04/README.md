# misis_python
# `Лабораторная работа 4`

### Запуск (из корня проекта)
python src/lab04/text_report.py --in data/input.txt --out data/report.csv
Для другой кодировки: добавьте --encoding cp1251

### `Краевые случаи (политика поведения)`
1. Файл не существует: выводится "Файл не найден: <путь>", скрипт завершается с кодом 1 (без traceback).

![](/images/lab04/img04.png)
2. Пустой вход: программа не падает, report.csv создается и содержит только word,count.

![](/images/lab04/img03.png) ![](/images/lab04/img05.png)

3. Для нестандартной кодировки (не UTF-8): кодировка cp1251 -> добавьте флаг: --encoding cp1251 (python src/lab04/text_report.py --encoding cp1251).


## `Задание A: io_txt_csv.py`
Функции read_text (чтение) и write_csv (запись с проверкой длины строк).

## `Задание B: text_report.py`
Скрипт читает текст, считает частоты (lib.text), сортирует (count ↓, слово ↑) и создаёт CSV. Выводит Топ-5 в консоль.

![](/images/lab04/img01.png)
![](/images/lab04/img02.png)
