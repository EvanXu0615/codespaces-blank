import copy
import csv

def REF(matrix, row, col):
    row_count = len(matrix) - row
    if (row_count <= 0):
        return matrix
    col_count = len(matrix[row]) - col
    if (col_count <= 0):
        return matrix
    base_row = []
    base = -1
    for i in range(row, row + row_count):
        if (matrix[i][col] != 0):
            base_row = matrix[i]
            base = i
            break
    matrix[base] = matrix[row]
    matrix[row] = base_row;
    pivot = matrix[row][col]
    for i in range(col, col + col_count):
        matrix[row][i] /= pivot
    for i in range(row + 1, row + row_count):
        scale = matrix[i][col]
        for j in range(col, col + col_count):
            matrix[i][j] -= matrix[row][j] * scale
    return REF(matrix, row + 1, col + 1)


row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3]

def areEqual(matrix_1, matrix_2):
    row_1 = len(matrix_1)
    col_1 = len(matrix_1[0])
    row_2 = len(matrix_2)
    col_2 = len(matrix_2[0])
    if (not (row_1 == row_2)):
        return False
    if (not (col_1 == col_2)):
        return False
    for i in range(row_1):
        for j in range(col_1):
            if (not (matrix_1 == matrix_2)):
                return False
    return True
    

def areRowEquivalent(matrix_1, matrix_2):
    new_matrix_1 = REF(matrix_1, 0, 0), matrix_1, matrix_1[0])
    new_matrix_2 = REF(matrix_2, 0, 0), matrix_2, matrix_2[0])
    return areEqual(new_matrix_1, new_matrix_2)

with open("matrix.txt") as f:
    reader = csv.reader(f)
    d = list(reader)

r = len(d)
c = len(d[0])
for i in range(r):
  for j in range(c):
    d[i][j]=float(d[i][j])

row_1 = [1, 2, 3, 4.2]
row_2 = [5, -6, 0, 1]
row_3 = [6, -7, .2, 2]

e = [row_1, row_2, row_3]

print(areRowEquivalent(e, d))
