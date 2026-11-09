def linear_search(nums, x):
    """Индекс первого вхождения x или -1."""
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums, x):
    """Индекс x в отсортированном списке или -1.
    На неотсортированном списке результат не определён."""
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def two_sum_brute(nums, target):
    """Пара индексов (i, j) или None."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target):
    """То же через словарь за один проход."""
    seen = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return (seen[need], i)
        seen[nums[i]] = i
    return None
