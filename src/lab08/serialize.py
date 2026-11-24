import json
from pathlib import Path

from src.lab08.models import student_from_dict, student_to_dict


def students_to_json(students: list[dict], path: str | Path) -> None:
    """Сериализует список записей студентов в JSON-файл."""
    if not isinstance(students, list):
        raise ValueError("Ожидался список записей студентов (list[dict])")

    serialized = [student_to_dict(student) for student in students]
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(serialized, file, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[dict]:
    """Десериализует список студентов из JSON-файла (политика strict)."""
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as file:
        raw_data = json.load(file)

    if not isinstance(raw_data, list):
        raise ValueError("Корневой элемент JSON должен быть списком объектов")

    students: list[dict] = []
    for index, item in enumerate(raw_data, start=1):
        try:
            student = student_from_dict(item)
        except ValueError as err:
            raise ValueError(f"Ошибка валидации в записи №{index}: {err}") from err
        students.append(student)

    return students