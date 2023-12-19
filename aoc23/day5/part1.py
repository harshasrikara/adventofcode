import sys

def get_seeds(line: str) -> list[int]:
    line = line[7:]
    seeds = line.split(" ")
    seeds = [int(x) for x in seeds]

    seed_start = []
    seed_range = []
    for i in range(len(seeds)):
        if i % 2 == 0:
            seed_start.append(seeds[i])
        else:
            seed_range.append(seeds[i])

    new_seed_list = []
    for i in range(len(seed_start)):
        print(f"done with {i}/{len(seed_start)}")
        for j in range(seed_range[i]):
            new_seed_list.append(seed_start[i] + j)
    return new_seed_list


def get_keys(line: str) -> [str, str]:
    terms = line.split(" ")
    keys = terms[0].split("-to-")
    return keys[0], keys[1]

def get_numbers(line: str) -> [int, int, int]:
    terms = line.split(" ")
    return int(terms[0]), int(terms[1]), int(terms[2])

def parse(file):
    hash_map = {}
    source_arr = []
    destination_arr = []
    range_arr = []

    key1, key2 = "", ""
    source, destination, range = 0,0,0
    seeds = []
    convert_keys = []
    for line in file.readlines():
        line = line.strip('\n')
        # print(line)

        # print(line)
        if line == "":
            if range == 0:
                continue
            
            hash_map[key1 + key2] = [source_arr, destination_arr, range_arr]

            # print(hash_map)
            source_arr = []
            destination_arr = []
            range_arr = []
            key1, key2 = "", ""
            source, destination, range = 0,0,0

        elif "seeds" in line:
            seeds = get_seeds(line)
            print(seeds)
        elif "map" in line:
            key1, key2 = get_keys(line)
            convert_keys.append(key1+key2)
            # print(key1)
            # print(key2)
        else:
            destination, source, range = get_numbers(line)
            source_arr.append(source)
            destination_arr.append(destination)
            range_arr.append(range)
            # print(source)
            # print(destination)
            # print(range)

    return hash_map, convert_keys, seeds

def convert(conversion_table: dict[str, list[list[int]]], src: str, value: int) -> int:
            source, destination, ranges = list(conversion_table[src][0]), conversion_table[src][1], conversion_table[src][2]

            new_val = value
            for i in range(len(source)):
                 if value >= source[i] and value < source[i] + ranges[i]:
                    diff = value - source[i]
                    new_val = destination[i] + diff
            

            return new_val


def main() -> int:
    f = open("/Users/harshasrikara/aoc23/day5/input.txt")

    conv, convert_keys, seeds = parse(f)
    # print(conv)

    
    arr = []
    for seed in seeds:
        value = seed
        for key in convert_keys:
            value = convert(conv, key, value)
        
        arr.append(value)
    
    # print(arr)
    print(min(arr))

    return 0


if __name__ == '__main__':
    sys.exit(main())