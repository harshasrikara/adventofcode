# This is all boilerplate
file1 = open('../res/advent_7.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)

class Node:
    color = ""

    def __init__(self):
        self.color = ""

for row in rows:
    vals = row.split("contain")
    child = vals[1]
    first = vals[0].split(" ")
    parent_bag_color = first[0] + " " +  first[1]
    print(row, end='')
    print("parent bag color: " + parent_bag_color)
    if "no other" in child:
        continue


# Figure out how many possible bags can
# contain shiny gold bags

# blue bags contain red bags
# red bags contain shiny gold bags

# 2

# Needs some graph theory thinking
