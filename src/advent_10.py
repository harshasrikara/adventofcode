file1 = open('../res/advent_10.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)

nums = []

for row in rows:
    nums.append(int(row))

nums.sort()
one_diff = 1
two_diff = 0
three_diff = 1

print(nums)

for i in range(len(nums) - 1):
    if nums[i + 1] - nums[i] == 1:
        one_diff = one_diff + 1
    if nums[i + 1] - nums[i] == 2:
        two_diff = two_diff + 1
    if nums[i + 1] - nums[i] == 3:
        three_diff = three_diff + 1

print("product: " + str(one_diff * three_diff))
