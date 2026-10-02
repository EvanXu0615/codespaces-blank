import csv

with open("matrix.txt") as f:
    reader = csv.reader(f)
    d = list(reader)

r = len(d)
c = len(d[0])
for i in range(r):
  for j in range(c):
    d[i][j]=float(d[i][j])

row_1 = [1, 2, 3, 4]
row_2 = [0, 1, 2, 3]
row_3 = [0, 0, 0, 0]
e_matrix = [row_1, row_2, row_3]

def isRowZero(row):
    for i in range(len(row)):
        if (row[i] != 0):
            return False
    return True
def isRowEchelon(matrix):
    for i in range(c):
        if (i < r and matrix[i][i] == 0 and not isRowZero(matrix[i])):
            return False
        for j in range(i + 1, r):
            if (matrix[j][i] != 0):
                return False
    return True
print(isRowEchelon(d))
print(isRowEchelon(e_matrix))
