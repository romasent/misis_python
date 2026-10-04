def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat and any(len(row) != len(mat[0]) for row in mat):
        raise ValueError("рваная матрица")

    return [list(col) for col in zip(*mat)]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    if any(len(row) != len(mat[0]) for row in mat):
        raise ValueError("рваная матрица")

    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    if any(len(row) != len(mat[0]) for row in mat):
        raise ValueError("рваная матрица")

    return [sum(col) for col in zip(*mat)]


# Тесты transpose
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))

try:
    print(transpose([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)


# Тесты row_sums
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))

try:
    print(row_sums([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)


# Тесты col_sums
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))

try:
    print(col_sums([[1, 2], [3]]))
except ValueError as e:
    print("ValueError:", e)
