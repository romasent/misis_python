def format_record(rec: tuple[str, str, float]) -> str:

    if not isinstance(rec, tuple):
        raise TypeError("Запись должна быть кортежем")

    if len(rec) != 3:
        raise ValueError("В кортеже должно быть 3 элемента")

    if not isinstance(rec[0], str):
        raise TypeError("ФИО должно быть строкой")

    if not isinstance(rec[1], str):
        raise TypeError("Группа должна быть строкой")

    if not isinstance(rec[2], (int, float)) or isinstance(rec[2], bool):
        raise TypeError("GPA должна быть числом")

    fio = " ".join(rec[0].strip().split())
    group = rec[1].strip()
    gpa = rec[2]

    if len(fio.split()) not in (2, 3):
        raise ValueError("ФИО должно содержать 2 или 3 слова")

    if not group:
        raise ValueError("Группа не может быть пустой")

    if not 0 <= gpa <= 5:
        raise ValueError("GPA должна быть от 0 до 5")

    words = fio.split()

    surname = words[0].capitalize()
    initials = "".join(word[0].upper() + "." for word in words[1:])

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
