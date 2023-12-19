import sys

def calculate_ranges(time: int):
    dist_travelled = []
    for i in range(time):
        dist = i*(time-i)
        dist_travelled.append(dist)
    
    dist_travelled.append(0)
    # print(dist_travelled)
    return dist_travelled

def get_vals_above_threshold(distances, threshold):
    count = 0
    for dist in distances:
        if dist > threshold:
            count = count + 1
    
    # print(count)
    return count

def parse(file):
    for line in file.readlines():
        line = line.strip('\n')
        # print(line)

def main() -> int:
    f = open("/Users/harshasrikara/aoc23/day6/input.txt")

    times = [40929790]
    max_distances = [215106415051100]

    counts = 1
    for i in range(len(times)):
        distances = calculate_ranges(times[i])
        count = get_vals_above_threshold(distances, max_distances[i])

        counts = counts * count

    print(counts)
    return 0


if __name__ == '__main__':
    sys.exit(main())