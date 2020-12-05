file1 = open('../res/advent_5.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)


def get_fb_number(seat: str) -> int:
    print(seat)
    top_index = 127
    bottom_index = 0
    for char in seat:
        diff = top_index - bottom_index + 1
        if char == 'F':
            top_index = top_index - int(diff / 2)
        else:
            bottom_index = bottom_index + int(diff / 2)
    print("top index: " + str(top_index))
    print("bottom index: " + str(bottom_index))
    return top_index


def get_rl_number(seat: str) -> int:
    print(seat)
    top_index = 7
    bottom_index = 0
    for char in seat:
        diff = top_index - bottom_index + 1
        if char == 'L':
            top_index = top_index - int(diff / 2)
        else:
            bottom_index = bottom_index + int(diff / 2)
    print("top index: " + str(top_index))
    print("bottom index: " + str(bottom_index))
    return top_index


max_seat = 0
arr = []

for row in rows:
    fb = row[0:7]
    rl = row[7:10]
    seat_id = (get_fb_number(fb) * 8) + get_rl_number(rl)
    if seat_id > max_seat:
        max_seat = seat_id
    arr.append(seat_id)

arr.sort()
print(arr)

for i in range(len(arr) - 1):
    if arr[i] + 1 != arr[i + 1]:
        print(arr[i] + 1)
