
file1 = open('../res/advent_2021_2.txt', 'r')
Lines = file1.readlines() 

ll = []
copy_list = []
nex = []

for line in Lines:
    ll.append(line)

# ll = list(map(lambda x: int(x), ll))

forward_dist = 0
aim = 0
depth = 0

for dir in ll:
    words = dir.split(' ')
    direction = words[0]
    distance = int(words[1])

    if direction == "forward":
        forward_dist = forward_dist + distance
        depth = depth + (aim * distance)
    elif direction == "down":
        aim = aim + distance
    elif direction == "up":
        aim = aim - distance

print (forward_dist * depth)

