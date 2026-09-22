import ast

def transpose(mat):
    if mat and any(len(r) != len(mat[0]) for r in mat):
        raise ValueError("рваная матрица")
    return [list(col) for col in zip(*mat)]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    if any(len(r) != len(mat[0]) for r in mat):
        raise ValueError("рваная матрица")
    
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:

    if any(len(r) != len(mat[0]) for r in mat):
        raise ValueError("рваная матрица")
    return [sum(col) for col in zip(*mat)]
    

r = input("Введите матрицу (например, [[1,2], [3,4]]): ")
mat = ast.literal_eval(r)

try:
    print("Транспонированная матрица:", transpose(mat))
    print("Суммы по строкам:", row_sums(mat))
    print("Суммы по столбцам:", col_sums(mat))
except ValueError as e:
    print("ValueError: рваная матрица")
