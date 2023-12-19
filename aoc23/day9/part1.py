import sys

def parse(file: str):
    entries = []
    for line in file.readlines():
        line = line.strip('\n')
        print(line)

        nums = line.split(" ")
        nums = [int(x) for x in nums]

        entries.append(nums)

    return entries

def get_difference_list(entry: list[int]):
    diffs = []
    for i in range(len(entry) - 1):
        diffs.append(entry[i+1] - entry[i])

    return diffs

def check_for_zeroes(entry: list[int]):
    for val in entry:
        if val != 0:
            return False
        
    return True

def get_all_differences(entry: list[int]) -> list[list[int]]:

    history = [entry]
    next = get_difference_list(entry)
    while not check_for_zeroes(next):
        history.append(next)
        next = get_difference_list(next)
    
    next.append(0)
    history.append(next)

    return history

def get_predicted_value(entry: list[int]):

    history = get_all_differences(entry)

    for i in range(len(history)-1):
        history[-2-i].append(history[-2-i][-1] + history[-1-i][-1])
    
    return history[0][-1]

def get_backward_value(entry: list):
    history = get_all_differences(entry)

    for i in range(len(history)-1):
        history[-2-i].insert(0, history[-2-i][0] - history[-1-i][0])
    
    print(history)
    return history[0][0]

def main() -> int:
    f = open("/Users/harshasrikara/aoc23/day9/input.txt")

    entries = parse(f)

    total = 0
    for entry in entries:
        prediction = get_backward_value(entry)
        total = total + prediction

    print(total)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())