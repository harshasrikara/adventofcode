import statistics

file1 = open('../res/advent_2021_9.txt', 'r')
Lines = file1.readlines() 

ll = []

for line in Lines:
    ll.append(line)

matrix = []

for entry in ll:
    row = list(entry)
    matrix.append(row)

print(matrix)

for index in range(0, len(matrix)):
    for index2 in range(0, len(matrix)):
        matrix[index][index2] = int(matrix[index][index2])

def is_low_point(i, j):
    if i == 0 and j == 0:
        if matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j+1]:
            return True
        return False
    elif i == 0 and j == len(matrix) - 1:
        if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][j - 1]:
            return True
        return False
    elif i == len(matrix) - 1 and j == 0:
        if matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j + 1]:
            return True
        return False
    elif i == len(matrix) - 1 and j == len(matrix) - 1:
        if matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j - 1]:
            return True
        return False
    elif i == 0:
        if matrix[i][j] < matrix[i][j + 1] and matrix[i][j] < matrix[i][j - 1] and matrix[i][j] < matrix[i + 1][j]:
            return True
        return False
    elif j == 0:
        if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j + 1]:
            return True
        return False
    elif i == len(matrix) - 1:
        if matrix[i][j] < matrix[i][j + 1] and matrix[i][j] < matrix[i][j - 1] and matrix[i][j] < matrix[i - 1][j]:
            return True
        return False
    elif j == len(matrix) - 1:
        if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j - 1]:
            return True
        return False
    else:
        if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j + 1] and matrix[i][j] < matrix[i][j - 1]:
            return True
        return False
    return False

risk_count = 0

for index in range(0, len(matrix)):
    for index2 in range(0, len(matrix)):
        if is_low_point(index, index2):
            risk_count = risk_count + matrix[index][index2] + 1


print(risk_count)