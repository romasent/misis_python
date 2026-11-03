# misis_python
# Лабораторная работа №6

# ЛР6 — CLI-утилиты с argparse

## Модули
- `src/lab06/cli_text.py` — команды `cat` и `stats`.
- `src/lab06/cli_convert.py` — команды `json2csv`, `csv2json`, `csv2xlsx`.
- `src/lab06/__init__.py` — делает папку пакетом.

## Примеры запуска (из корня проекта)

### cli_text.py
```bash
python -m src.lab06.cli_text cat --input data/samples/people.txt -n
python -m src.lab06.cli_text stats --input data/samples/people.txt --top 3
cli_convert.py
```
### cli_convert.py
```bash
python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv
python -m src.lab06.cli_convert csv2json --in data/out/people.csv --out data/out/people2.json
python -m src.lab06.cli_convert csv2xlsx --in data/out/people.csv --out data/out/people.xlsx
```
### Справка
```bash
python -m src.lab06.cli_text --help
python -m src.lab06.cli_convert --help
python -m src.lab06.cli_text cat --help
python -m src.lab06.cli_convert json2csv --help
```
Описание команд и параметров
cat

--input (обязательный) — путь к текстовому файлу.

-n — нумеровать строки.
Выводит содержимое файла построчно.

stats

--input (обязательный) — путь к текстовому файлу.

--top (по умолчанию 5) — сколько самых частых слов вывести.
Считает частоты слов (без учета регистра).

json2csv

--in (обязательный) — входной JSON.

--out (обязательный) — выходной CSV.

csv2json

--in (обязательный) — входной CSV.

--out (обязательный) — выходной JSON.

csv2xlsx

--in (обязательный) — входной CSV.

--out (обязательный) — выходной XLSX.

Обработка ошибок
Отсутствие входного файла — сообщение в stderr, код возврата 1.

Бинарный файл (не текст) в cat/stats — UnicodeDecodeError, понятное сообщение.

Неверные аргументы — argparse выводит справку, код возврата 2.

--help работает для каждой подкоманды без ошибок.

Скриншоты

cat -n

stats --top

json2csv

csv2json

csv2xlsx

--help

