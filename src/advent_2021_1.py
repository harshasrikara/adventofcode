
file1 = open('../res/advent_2021_1.txt', 'r')
Lines = file1.readlines() 

ll = []
copy_list = []
nex = []

for line in Lines:
    ll.append(line)

ll = list(map(lambda x: int(x), ll))

count = 0

for index in range(3, len(ll)):
    sum1 = ll[index] + ll[index - 1] + ll[index-2]
    sum2 = ll[index -1] + ll[index - 2] + ll[index - 3]
    if (sum1 > sum2):
        count = count + 1
    print(ll[index])

print(count)


