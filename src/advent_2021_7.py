import statistics

file1 = open('../res/advent_2021_7.txt', 'r')
Lines = file1.readlines() 

ll = []

for line in Lines:
    ll.append(line)

ll[0] = '16,1,2,0,4,2,7,1,2,14'

nums = list(map(lambda x: int(x), ll[0].split(',')))

print(max(nums))

def calc_fuel(dist):
    total = 0
    for i in range(1, dist+1):
        total = total + i
    return total

min_total_fuel = 10000000000000000000000000

for i in range(0, max(nums)):
    total_fuel = 0
    for val in nums:
        fuel = calc_fuel(abs(i - val))
        total_fuel = total_fuel + fuel

    if total_fuel < min_total_fuel:
        min_total_fuel = total_fuel

print(calc_fuel(abs(5 - 16)))

print(min_total_fuel)