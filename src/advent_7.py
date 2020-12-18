# This is all boilerplate
from typing import List

file1 = open('../res/advent_7.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)

child_to_parent = {}
parent_to_child = {}

def extract_colors(sentence: str):
    vals = sentence.split("contain")
    child = vals[1]
    first = vals[0].split(" ")
    parent_bag_color = first[0] + " " + first[1]
    if "no other" in child:
        return parent_bag_color, []
    bags_full = child.split("bag")
    bag_array = []
    for bags in bags_full:
        if len(bags) < 5:
            continue
        words = bags.split(" ")
        child_color = words[2] + " " + words[3]
        bag_array.append(child_color)
    return parent_bag_color, bag_array


for row in rows:
    parent, child = extract_colors(row)
    # print(row, end='')
    # print("parent: " + parent)
    # print("child: " + str(child))
    # print()
    # attempt two to create big "baskets" of parent colors
    if parent in parent_to_child:
        for entry in child:
            if not entry in parent_to_child[parent]:
                parent_to_child[parent].append(entry)
    else:
        parent_to_child[parent] = []
        for entry in child:
            if not entry in parent_to_child[parent]:
                parent_to_child[parent].append(entry)

    # attempt one (the map works but the recursive part is eh
    for entry in child:
        if entry in child_to_parent:
            child_to_parent[entry].append(parent)
        else:
            child_to_parent[entry] = []
            child_to_parent[entry].append(parent)

# print(len(nodeset))

for entry in child_to_parent:
    print("child: " + entry)
    print("parent: " + str(child_to_parent[entry]))
    print()

initial = 'shiny gold'
unique_col = []

# this recursion is not working :/
def recursive(bag_color: str) -> int:
    sum = 0
    if not bag_color in child_to_parent:
        return 1
    for entry in child_to_parent[bag_color]:
        if not entry in unique_col:
            unique_col.append(entry)
            sum = sum + recursive(entry)
    return sum


total_color_count = recursive(initial)
print("total color count that doesn't work: " + str(total_color_count))

total = 0
for entry in parent_to_child:
    if 'shiny gold' in parent_to_child[entry]:
        total = total + 1

print("total bags w shiny: " + str(total))

# Figure out how many possible bags can
# contain shiny gold bags

# blue bags contain red bags
# red bags contain shiny gold bags

# 2

# Needs some graph theory thinking
