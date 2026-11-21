def bubble_sort(nums: list[int]) -> list[int]:
    """Новый список, отсортированный по возрастанию. Исходный не меняется.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    arr = list(nums)
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(nums: list[int]) -> list[int]:
    """Новый список, отсортированный по возрастанию вставками. Исходный не меняется."""
    arr = list(nums)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(nums: list[int]) -> list[int]:
    """Новый список, отсортированный по возрастанию выбором. Исходный не меняется."""
    arr = list(nums)
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Вспомогательное слияние двух отсортированных списков."""
    res: list[int] = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def merge_sort(nums: list[int]) -> list[int]:
    """(★) Итеративная сортировка слиянием снизу вверх (без рекурсии).
    Исходный список не меняется.
    """
    arr = list(nums)
    n = len(arr)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i : i + width]
            right = arr[i + width : i + 2 * width]
            arr[i : i + 2 * width] = _merge(left, right)
        width *= 2
    return arr


def counting_sort(nums: list[int], lo: int, hi: int) -> list[int]:
    """(★) Сортировка подсчётом для целых чисел в известном диапазоне [lo, hi].
    Исходный список не меняется.
    """
    if lo > hi:
        raise ValueError("Нижняя граница lo не может быть больше верхней hi")

    counts = [0] * (hi - lo + 1)
    for x in nums:
        if x < lo or x > hi:
            raise ValueError(f"Элемент {x} выходит за пределы диапазона [{lo}, {hi}]")
        counts[x - lo] += 1

    res: list[int] = []
    for idx, count in enumerate(counts):
        if count > 0:
            res.extend([lo + idx] * count)
    return res