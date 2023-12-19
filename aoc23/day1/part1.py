import regex as re
f = open("/Users/harshasrikara/aoc23/day1/p1.txt")

numberdict = {"zero": 0, "one": 1,"two": 2,"three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}

count = 0

sumo = 0
totals = []
for line in f.readlines():
    line = line.strip('\n')
    print(line)

    vals = re.findall('zero|one|three|four|five|six|two|seven|eight|nine|1|2|3|4|5|6|7|8|9|0', line, overlapped=True)
    print(vals)
    vals = [numberdict[x] if not x.isdigit() else int(x) for x in vals]

    print(vals)

    total = 0

    if len(vals) > 1:
        total = int(str(vals[0]) + str(vals[len(vals) - 1]))
    else:
        total = int(str(vals[0]) + str(vals[0]))

    print(total)
    totals.append(total)

    sumo = sumo + total

print(sumo)