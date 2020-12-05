file1 = open('../res/advent_2.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)

valid_count = 0

for row in rows:
    elements = row.split(" ")
    minmax = elements[0].split("-")
    min = minmax[0]
    max = minmax[1]
    letter = elements[1][0]
    password = elements[2]
    print("minimum: " + min)
    print("maximum: " + max)
    print("letter: " + letter)
    print("password: " + password)

    check = False
    if password[int(min) - 1] == letter:
        check = not check
    if password[int(max) - 1] == letter:
        check = not check
    
    if check:
        valid_count = valid_count + 1

    # letter_count = 0
    # for ch in password:
    #     if ch == letter:
    #         letter_count = letter_count + 1
    
    # if letter_count >= int(min) and letter_count <= int(max):
    #     valid_count = valid_count + 1

print("valid count: " + str(valid_count))
