
file1 = open('../res/advent_2021_3.txt', 'r')
Lines = file1.readlines() 

ll = []

for line in Lines:
    ll.append(line)

# ll = list(map(lambda x: int(x), ll))

counter = []

for i in range(0, len(ll[0])-1):
    counter.append({'0': 0, '1': 0})

for entry in ll:
    index = 0
    for bit in entry:
        if (bit != '\n'):
            counter[index][bit] = counter[index][bit] + 1
        # print(bit + ' ', end='')
        index = index + 1

# max = ''
# min = ''
#
# for count in counter:
#     if(count['0'] > count['1']):
#         max = max + '0'
#         min = min + '1'
#     else:
#         max = max + '1'
#         min = min + '0'
#
# print(max)
# print(min)
#
# print(int(max, 2))
# print(int(min, 2))

solutionsetMax = []
solutionsetMin = []
index = 0

while(len(solutionsetMax) != 1):
    solutionsetMax = []

    maxbit = ''
    minbit = ''

    if (counter[index]['1'] >= counter[index]['0']):
        maxbit = '1'
        minbit = '0'
    else:
        maxbit = '0'
        minbit = '1'

    for entry in ll:
        if (entry[index] == maxbit):
            solutionsetMax.append(entry)

    if (len(solutionsetMax) == 1):
        break

    index = index + 1
    ll = solutionsetMax

print(solutionsetMax)

