import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать файл в указанной кодировке (по умолчанию UTF-8).
    Возвращает содержимое файла одной строкой.
    """
    return Path(path).read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """Записать строки в CSV (UTF-8, разделитель ``,``).
    Если передан header, пишется первой строкой.
    Поднимает ValueError, если строки в rows имеют разную длину.
    """
    rows = list(rows)
    lengths = {len(r) for r in rows}
    if len(lengths) > 1:
        raise ValueError(f"Строки разной длины: {sorted(lengths)}")

    with Path(path).open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
