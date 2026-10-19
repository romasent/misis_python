# misis_python
# Лабораторная работа 4

## Запуск (из корня проекта)
python src/lab04/text_report.py --in data/input.txt --out data/report.csv
Для другой кодировки: добавьте --encoding cp1251

## Политики
- Пустой вход: создается CSV только с заголовком word,count.
- Нет файла: вывод ошибки, код возврата 1.
- По умолчанию: UTF-8, разделитель ",".

## Задание A: io_txt_csv.py
Функции read_text (чтение) и write_csv (запись с проверкой длины строк).
![](images/lab04/img01.png)

## Задание B: text_report.py
Скрипт читает текст, считает частоты (lib.text), сортирует (count ↓, слово ↑) и создаёт CSV. Выводит Топ-5 в консоль.
![](images/lab04/img02.png)
