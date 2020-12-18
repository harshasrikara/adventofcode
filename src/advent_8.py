file1 = open('../res/advent_8.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)

past_index = []

index = 0
accumulator = 0
while True:
    if index in past_index:
        break
    if index == 640 and rows[index].split(" ")[0] != "jmp":
        break
    action = ""
    action = rows[index].split(" ")[0]
    value = 0
    if "+" in rows[index]:
        value = int(rows[index].split(" ")[1].split("+")[1])
    else:
        value = int(rows[index].split(" ")[1].split("-")[1]) * -1
    past_index.append(index)
    if action == "nop":
        accumulator = accumulator
        index = index + 1
    elif action == "acc":
        accumulator = accumulator + value
        index = index + 1
    elif action == "jmp":
        index = index + value

print("accumulator: " + str(accumulator))