import regex as re

f = open("/Users/harshasrikara/aoc23/day2/input.txt")

constraint = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def get_colors(round: str):
    colors = round.split(',')

    output = {}

    for color in colors:
        values = color.split(' ')
        values = [x for x in values if x != '']
        output[values[1]] = int(values[0])
    
    return output

arr = []
count = 1
tally = 0
for line in f.readlines():
    line = line.strip('\n')
    print(line)

    condensed_line = line[8:]

    rounds = condensed_line.split(';')
    rounds = [get_colors(x) for x in rounds]

    success = True

    min = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for round in rounds:
        print(round)

        for key in round:
            if round[key] > min[key]:
                min[key] = round[key]
        
        # for key in round:
        #     if round[key] > constraint[key]:
        #         success = False
    
    power = min["red"] * min["green"] * min["blue"]
    tally = tally + power

    count = count + 1

print(tally)