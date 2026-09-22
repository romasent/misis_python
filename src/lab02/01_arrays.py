def min_max(*nums) -> tuple[float | int, float | int]:
    if len(nums) == 1 and isinstance(nums[0], (list, tuple)):
        nums = nums[0]
    if not nums:
        raise ValueError("Список пуст")
    return min(nums), max(nums)


def unique_sorted(*nums) -> list[float | int]:
    if len(nums) == 1 and isinstance(nums[0], (list, tuple)):
        nums = nums[0]
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    sp = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError("строка не строка строк матрицы")
        for item in i:
            sp.append(item)
    return sp


print(min_max(3, -1, 5, 5, 0))
print(min_max(42))
try:
    print(min_max())
except ValueError as e:
    print(f"ValueError: {e}")
print(min_max(1.5, 2, 2.0, -3.1))

print(unique_sorted(3, 1, 2, 1, 3))
print(unique_sorted())
print(unique_sorted(-1, -1, 0, 2, 2))
print(unique_sorted(1.0, 1, 2.5, 2.5, 0))

print(flatten([[1, 2], [3, 4]]))
print(flatten([]))
print(flatten([[1], [], [2, 3]]))
try:
    print(flatten([[1, 2], "ab"]))
except TypeError as e:
    print(f"TypeError: {e}")
