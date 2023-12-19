
file1 = open('../res/advent_2021_6.txt', 'r')
Lines = file1.readlines() 

ll = []

for line in Lines:
    ll.append(line)

nums = ll[0].split(',')

print(nums)

num_arr = []

for x in nums:
    num_arr.append(int(x))

def compute_iteration(arr):
    zero_counter = 0
    for index in range(0, len(arr)):
        if (arr[index] == 0):
            zero_counter = zero_counter + 1
            arr[index] = 6
        else:
            arr[index] = arr[index] - 1
    return zero_counter, arr


for i in range(0, 256):
    print(i)
    count, new_arr = compute_iteration(num_arr)
    num_arr = new_arr
    for j in range(0, count):
        num_arr.append(8)

print(len(num_arr))