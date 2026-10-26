# misis_python

# Лабораторная работа 5
## JSON и конвертации (JSON↔CSV, CSV→XLSX)

* `src/lab05/json_csv.py` — функции `json_to_csv` и `csv_to_json` (только `json`, `csv`, `pathlib`).
* `src/lab05/csv_xlsx.py` — функция `csv_to_xlsx` (через `openpyxl`, автоширина колонок, лист `Sheet1`).
* `src/lab05/run_demo.py` — скрипт для демонстрации функций.

## Допущения
* Кодировка файлов: **UTF-8**.
* Порядок колонок JSON→CSV: по ключам первого объекта.
* Значения CSV→JSON: сохраняются как строки.
* Ошибки: нет файла → `FileNotFoundError`; пустой/битый файл → `ValueError`.
* XLSX: Используется библиотека openpyxl. Первая строка — заголовок, лист "Sheet1". Автоширина колонок рассчитывается по самому длинному тексту, но не менее 8 символов.

## Запуск 3-х конвертаций сразу с установкой зависимостей.
```bash
python -m pip install -r requirements.txt
python -m src.lab05.run_demo
```
![](/images/lab05/img01.png)

##
![](/images/lab05/img02.png)
## people.csv -> people_from_csv.json
![](/images/lab05/img03.png)
## people.json -> people_from_json.csv
![](/images/lab05/img04.png)
## cities.csv -> cities.xlsx
![](/images/lab05/img05.png)
