file1 = open('../res/advent_9.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)

def does_sum_exist(index, sum) -> bool:
    match = False
    lower_bound = max(0, index-25)
    for i in range(index - lower_bound):
        for j in range(index - lower_bound):
            if int(rows[lower_bound + i]) + int(rows[lower_bound + j]) == sum:
                match = True
    return match

point = 0

for row in rows:
    print(str(point) + " " + str(does_sum_exist(point, int(row))))
    point = point + 1

