file1 = open('../res/advent_2021_4.txt', 'r')
Lines = file1.readlines() 

ll = []

for line in Lines:
    ll.append(line)

bingo_nums = list(map(lambda x: int(x), ll[0].split(',')))

print(bingo_nums)

