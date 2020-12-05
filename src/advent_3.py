file1 = open('../res/advent_5.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)

tree_count = 0
x = 0
y = 0
x_increment = 3
row_max_len = 0

# print(len(rows))

for row in rows:
    row_max_len = len(row)
    if x >= row_max_len:
        x = x % 31
    if row[x] == '#':
        print("look: " + row[x])
        tree_count = tree_count + 1
    print("row: " + row, end='')
    print("x count: " + str(x))
    print("y count: " + str(y))
    print("tree count: " + str(tree_count))
    print("max len: " + str(row_max_len))
    print("-----------------------------------------------------")
    x = x + x_increment
    y = y + 1

print("total trees: " + str(tree_count))
# import math
# grid = [l.strip() for l in open('advent_3.txt')]
# res = [sum(grid[v][right*idx % len(grid[0])] == '#' for idx,v in enumerate(range(0, len(grid), down)))
#    for right, down in ([1,1], [3,1], [5,1], [7,1], [1,2])]
# print(f"Part 1: {res[1]}\nPart 2: {math.prod(res)}")


# file1 = open('advent_5.txt', 'r')
# Lines = file1.readlines()

# rows = []
# tree_count = 0
# x = 0
# y = 0
# x_increment = 3
# row_max_len = 0

# for line in Lines:
#     row_max_len = len(line)
#     if x >= row_max_len:
#         x = x - 31
#     if line[x] != '.':
#         print("look: " + line[x])
#         tree_count = tree_count + 1
#     print("row: " + line)
#     print("x count: " + str(x))
#     print("y count: " + str(y))
#     print("tree count: " + str(tree_count))
#     print("max len: " + str(row_max_len))
#     print("-----------------------------------------------------")
#     x = x + x_increment
#     y = y + 1

# print("total trees: " + str(tree_count))