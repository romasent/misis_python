"""Демонстрация всех трёх конвертаций."""
from pathlib import Path

from src.lab05 import json_to_csv, csv_to_json, csv_to_xlsx

BASE = Path(__file__).resolve().parents[2]
SAMPLES = BASE / "data" / "samples"
OUT = BASE / "data" / "out"
OUT.mkdir(parents=True, exist_ok=True)

json_to_csv(SAMPLES / "people.json", OUT / "people_from_json.csv")
csv_to_json(SAMPLES / "people.csv", OUT / "people_from_csv.json")
csv_to_xlsx(SAMPLES / "cities.csv", OUT / "people.xlsx")

print("Готово:", *OUT.iterdir(), sep="\n")
