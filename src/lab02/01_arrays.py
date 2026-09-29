def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")

    minimum = nums[0]
    maximum = nums[0]

    for num in nums:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique = []

    for num in nums:
        if num not in unique:
            unique.append(num)

    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if unique[i] > unique[j]:
                unique[i], unique[j] = unique[j], unique[i]

    return unique


def flatten(mat: list[list | tuple]) -> list:
    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Элемент матрицы должен быть списком или кортежем")

        for item in row:
            result.append(item)

    return result


# Тесты min_max
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))

# Вывод ValueError при смешанном вводе строки
try:
    print(min_max([]))
except ValueError as e:
    print(f"ValueError: {e}")

print(min_max([1.5, 2, 2.0, -3.1]))


# Тесты unique_sorted
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


# Тесты flatten
print(flatten([[1, 2], [3, 4]]))
print(flatten([]))
print(flatten([[1], [], [2, 3]]))

# Вывод TypeError при смешанном вводе строки
try:
    print(flatten([[1, 2], "ab"]))
except TypeError as e:
    print(f"TypeError: {e}")
