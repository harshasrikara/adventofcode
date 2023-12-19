import sys
import math

size = 198

def parse(file):
    sum = 0
    for line in file.readlines():
        line = line.strip('\n')

        line = line[10:]
        print(line)

        sets = line.split("|")

        winning = sets[0].split(" ")
        selected = sets[1].split(" ")

        winning = set([x for x in winning if x != ""])
        selected = set([x for x in selected if x != ""])

        print(winning)
        print(selected)

        overlap = winning.intersection(selected)

        print(overlap)
        print(len(overlap))
        print(2**(len(overlap)-1))

        if len(overlap) == 0:
            print()
        else:
            sum = sum + (2**(len(overlap)-1))

    
    print(sum)

def part2(file):
    counts = [1 for x in range(size)]
    print(counts)

    current = 0
    for line in file.readlines():
        line = line.strip('\n')

        line = line[10:]
        print(line)

        sets = line.split("|")

        winning = sets[0].split(" ")
        selected = sets[1].split(" ")

        winning = set([x for x in winning if x != ""])
        selected = set([x for x in selected if x != ""])

        overlap = winning.intersection(selected)

        print(len(overlap))

        copies = counts[current] * len(overlap)

        for i in range(len(overlap)):
            counts[current + i + 1] = counts[current + i + 1] + counts[current]
        
        print(counts)

        current = current + 1

    total = sum(counts)
    print(counts)
    print(total)



def main() -> int:
    f = open("/Users/harshasrikara/aoc23/day4/input.txt")

    part2(f)

    return 0


if __name__ == '__main__':
    sys.exit(main())