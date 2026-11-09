import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__}: {nums} -> {result}"
        assert nums == original, f"{fn.__name__} изменила исходный: {nums}"


def check_search():
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-150, 150)
        expected = nums.index(x) if x in nums else -1
        assert linear_search(nums, x) == expected, f"linear: {nums}, x={x}"

    for _ in range(100):
        n = random.randint(0, 50)
        nums = sorted(random.randint(-100, 100) for _ in range(n))
        x = random.randint(-150, 150)
        idx = binary_search(nums, x)
        if idx == -1:
            assert x not in nums, f"binary: {nums}, x={x}"
        else:
            assert nums[idx] == x, f"binary: {nums}, x={x}, idx={idx}"


def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)
        b = two_sum_brute(nums, target)
        f = two_sum_fast(nums, target)
        assert (b is None) == (f is None), f"{nums}, target={target}: {b} vs {f}"
        for pair in (b, f):
            if pair is not None:
                i, j = pair
                assert i < j and nums[i] + nums[j] == target


if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK")
