import random

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import (
    bubble_sort,
    counting_sort,
    insertion_sort,
    merge_sort,
    selection_sort,
)


def check_sorting(fn, trials: int = 100) -> int:
    """Проверяет функцию сортировки на trials случайных списках."""
    checks = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список {original}"
        checks += 1
    return checks


def check_search(trials: int = 100) -> int:
    """Проверяет linear_search и binary_search против list.index и краевых случаев."""
    checks = 0
    # Краевые случаи для бинарного и линейного поиска
    edge_cases = [
        ([], 5),
        ([5], 5),
        ([5], 1),
        ([1, 3], 1),
        ([1, 3], 3),
        ([1, 3], 2),
        ([2, 2, 2, 2], 2),
    ]
    for arr, x in edge_cases:
        expected_first = arr.index(x) if x in arr else -1
        got_lin = linear_search(arr, x)
        assert got_lin == expected_first, f"linear_search({arr}, {x}) -> {got_lin}, ожидалось {expected_first}"

        got_bin = binary_search(arr, x)
        if x in arr:
            assert 0 <= got_bin < len(arr) and arr[got_bin] == x, (
                f"binary_search({arr}, {x}) -> {got_bin}"
            )
        else:
            assert got_bin == -1, f"binary_search({arr}, {x}) -> {got_bin}, ожидалось -1"
        checks += 2

    # Случайные проверки
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-30, 30) for _ in range(n)]
        target = random.randint(-35, 35)

        expected = nums.index(target) if target in nums else -1
        got_lin = linear_search(nums, target)
        assert got_lin == expected, f"linear_search({nums}, {target}) -> {got_lin}, ожидалось {expected}"
        checks += 1

        s_nums = sorted(nums)
        got_bin = binary_search(s_nums, target)
        if target in s_nums:
            assert 0 <= got_bin < len(s_nums) and s_nums[got_bin] == target, (
                f"binary_search({s_nums}, {target}) -> {got_bin}"
            )
        else:
            assert got_bin == -1, f"binary_search({s_nums}, {target}) -> {got_bin}, ожидалось -1"
        checks += 1

    return checks


def check_two_sum(trials: int = 100) -> int:
    """Сравнивает two_sum_brute и two_sum_fast на случайных данных."""
    checks = 0
    for _ in range(trials):
        n = random.randint(0, 40)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        if res_brute is None:
            assert res_fast is None, (
                f"Расхождение на {nums}, target={target}: brute=None, fast={res_fast}"
            )
        else:
            assert res_fast is not None, (
                f"Расхождение на {nums}, target={target}: brute={res_brute}, fast=None"
            )
            i, j = res_fast
            assert 0 <= i < j < len(nums) and nums[i] + nums[j] == target, (
                f"Некорректные индексы fast={res_fast} на {nums}, target={target}"
            )
        checks += 1
    return checks


if __name__ == "__main__":
    random.seed(42)
    total_checks = 0
    for sort_fn in (
        bubble_sort,
        insertion_sort,
        selection_sort,
        merge_sort,
        lambda a: counting_sort(a, -100, 100),
    ):
        total_checks += check_sorting(sort_fn, trials=100)

    total_checks += check_search(trials=100)
    total_checks += check_two_sum(trials=100)
    print(f"OK: {total_checks} проверок")