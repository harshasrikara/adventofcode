file1 = open('../res/advent_11.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)

seats = []

for row in rows:
    s_row = []
    for seat in row:
        if seat != "\n":
            s_row.append(seat)
    seats.append(s_row)

def print_seats():
    for seat in seats:
        for s in seat:
            print(s, end='')
        print()
    print()

print_seats()