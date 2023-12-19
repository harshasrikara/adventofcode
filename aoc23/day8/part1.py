import sys
from math import gcd

def parse(file: str) -> [str, dict[str, list[str]]]:
    node_mapping = {}
    path = ""
    for line in file.readlines():
        line = line.strip('\n')
        print(line)

        if "LRRRL" in line:
            path = line

        if "=" not in line:
            continue

        terms = line.split(" = (")
        origin = terms[0]

        terms = terms[1].split(", ")
        left = terms[0]
        right = terms[1][0:3]

        node_mapping[origin] = [left, right]
    
    return path, node_mapping

def count_steps(path: str, mapping: dict[str, list[str]]) -> int:

    current = "AAA"
    count = 0
    while True:
        for letter in path:
            if letter == "L":
                current = mapping[current][0]
            if letter == "R":
                current = mapping[current][1]
            
            count = count + 1

            if current == "ZZZ":
                return count
    return 0


def check_ends_with_z(nodes: list[str]) -> bool:
    for node in nodes:
        if node[-1] != "Z":
            return False
    
    return True

def count_parallel_steps(nodes: list[str], path: str, mapping: dict[str, list[str]]) -> [int]:
    current = nodes
    count = 0
    counts = []
    status = [True for x in range(6)]
    print(status)
    while True:
        for letter in path:
            new_list = []

            for node in current:
                if letter == "L":
                    new_list.append(mapping[node][0])
                if letter == "R":
                    new_list.append(mapping[node][1])
            
            count = count + 1

            for i in range(6):
                if(new_list[i][-1] == "Z"):
                    if status[i]:
                        print([i, count])
                        counts.append(count)
                    status[i] = False

                    if len(counts) == 6:
                        return counts

            if(check_ends_with_z(new_list)):
                return count
            
            current = new_list



def find_nodes_ending_in_a(mapping: dict[str, list[str]]) -> list[str]:
    ends_in_a = []
    for key in mapping:
        if key[-1] == "A":
            ends_in_a.append(key)

    return ends_in_a

def lcm(nums):
    lcm = 1
    for i in nums:
        lcm = lcm*i//gcd(lcm, i)
    
    return lcm

def main() -> int:
    f = open("/Users/harshasrikara/aoc23/day8/input.txt")

    path, mapping = parse(f)

    print(path)
    print(mapping)

    count = count_steps(path, mapping)

    print(count)

    ends_in_a = find_nodes_ending_in_a(mapping)

    print(ends_in_a)

    counts = count_parallel_steps(ends_in_a, path, mapping)

    print(lcm(counts))
    
    return 0


if __name__ == '__main__':
    sys.exit(main())