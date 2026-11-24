from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def validate_student(rec: dict) -> None:
    """Проверяет структуру словаря студента и корректность всех полей."""
    if not isinstance(rec, dict):
        raise ValueError("Запись студента должна быть словарём (dict)")

    if set(rec.keys()) != set(STUDENT_FIELDS):
        missing = set(STUDENT_FIELDS) - set(rec.keys())
        extra = set(rec.keys()) - set(STUDENT_FIELDS)
        raise ValueError(
            f"Неверный набор ключей. Пропущены: {missing or 'нет'}, лишние: {extra or 'нет'}"
        )

    fio = rec["fio"]
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError("Поле 'fio' должно быть непустой строкой")

    group = rec["group"]
    if not isinstance(group, str) or not group.strip():
        raise ValueError("Поле 'group' должно быть непустой строкой")

    birthdate = rec["birthdate"]
    if not isinstance(birthdate, str):
        raise ValueError("Поле 'birthdate' должно быть строкой формата YYYY-MM-DD")

    try:
        parsed_date = date.fromisoformat(birthdate)
    except ValueError as err:
        raise ValueError(
            f"Поле 'birthdate' содержит некорректную дату '{birthdate}': {err}"
        ) from err

    if parsed_date > date.today():
        raise ValueError(f"Дата рождения '{birthdate}' не может быть в будущем")

    gpa = rec["gpa"]
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise ValueError("Поле 'gpa' должно быть числом (int или float)")

    if not (0 <= gpa <= 5):
        raise ValueError(f"Поле 'gpa' должно быть в диапазоне от 0 до 5, получено: {gpa}")


def make_student(fio: str, birthdate: str, group: str, gpa: int | float) -> dict:
    """Создаёт и валидирует словарь-запись студента."""
    normalized_gpa = float(gpa) if isinstance(gpa, int) and not isinstance(gpa, bool) else gpa

    record = {
        "fio": fio.strip() if isinstance(fio, str) else fio,
        "birthdate": birthdate,
        "group": group.strip() if isinstance(group, str) else group,
        "gpa": normalized_gpa,
    }
    validate_student(record)
    return record


def student_age(rec: dict, today: date | None = None) -> int:
    """Возвращает количество полных лет студента на дату today."""
    validate_student(rec)
    birth = date.fromisoformat(rec["birthdate"])
    current_date = today if today is not None else date.today()

    if birth > current_date:
        raise ValueError(
            f"Дата рождения '{birth}' позже контрольной даты '{current_date}'"
        )

    had_birthday = (current_date.month, current_date.day) >= (birth.month, birth.day)
    return current_date.year - birth.year - (0 if had_birthday else 1)


def _age_word(age: int) -> str:
    """Возвращает корректное склонение слова 'год/года/лет'."""
    if 11 <= age % 100 <= 14:
        return "лет"
    last_digit = age % 10
    if last_digit == 1:
        return "год"
    if 2 <= last_digit <= 4:
        return "года"
    return "лет"


def format_student(rec: dict) -> str:
    """Форматирует запись студента в строку: Иванов И.И. (БИВТ-26-6-1), 19 лет, GPA 4.30."""
    validate_student(rec)
    parts = rec["fio"].split()
    surname = parts[0]
    initials = "".join(f"{part[0].upper()}." for part in parts[1:])
    short_fio = f"{surname} {initials}".strip()

    age = student_age(rec)
    return f"{short_fio} ({rec['group']}), {age} {_age_word(age)}, GPA {rec['gpa']:.2f}"


def student_to_dict(rec: dict) -> dict:
    """Возвращает валидированную копию словаря студента для сериализации."""
    validate_student(rec)
    return {
        "fio": rec["fio"],
        "birthdate": rec["birthdate"],
        "group": rec["group"],
        "gpa": float(rec["gpa"]),
    }


def student_from_dict(d: dict) -> dict:
    """Десериализует словарь в запись студента с приведением gpa к float и валидацией."""
    if not isinstance(d, dict):
        raise ValueError("Ожидался словарь для десериализации студента")

    if set(d.keys()) != set(STUDENT_FIELDS):
        missing = set(STUDENT_FIELDS) - set(d.keys())
        extra = set(d.keys()) - set(STUDENT_FIELDS)
        raise ValueError(
            f"Неверный набор ключей при десериализации. Пропущены: {missing or 'нет'}, лишние: {extra or 'нет'}"
        )

    raw_gpa = d["gpa"]
    normalized_gpa = (
        float(raw_gpa)
        if isinstance(raw_gpa, int) and not isinstance(raw_gpa, bool)
        else raw_gpa
    )

    record = {
        "fio": d["fio"].strip() if isinstance(d["fio"], str) else d["fio"],
        "birthdate": d["birthdate"],
        "group": d["group"].strip() if isinstance(d["group"], str) else d["group"],
        "gpa": normalized_gpa,
    }
    validate_student(record)
    return record