file1 = open('../res/advent_2021_10.txt', 'r')
Lines = file1.readlines()

ll = []

for line in Lines:
    ll.append(line)

for index in range(0, len(ll)):
    ll[index] = ll[index].rstrip()


score = 0

rever = {'[': ']', '{': '}', '(': ')', '<': '>'}

for entry in ll:
    stac = []
    for char in entry:
        if char == '{' or char == '[' or char == '(' or char == '<':
            stac.append(char)
        elif rever[stac[len(stac) - 1]] == char:
            stac.pop()
        else:
            if char == ')':
                score = score + 3
                break
            if char == ']':
                score = score + 57
                break
            if char == '}':
                score = score + 1197
                break
            if char == '>':
                score = score + 25137
                break

print(score)

def is_corrupted(entry):
    for char in entry:
        if char == '{' or char == '[' or char == '(' or char == '<':
            stac.append(char)
        elif rever[stac[len(stac) - 1]] == char:
            stac.pop()
        else:
            if char == ')':
                return True
            if char == ']':
                return True
            if char == '}':
                return True
            if char == '>':
                return True
    return False

new_arr = []

for entry in ll:
    if is_corrupted(entry) == False:
        new_arr.append(entry)

score_list = []

for entry in new_arr:
    stac = []
    score = 0
    for char in entry:
        if char == '{' or char == '[' or char == '(' or char == '<':
            stac.append(char)
        elif rever[stac[len(stac) - 1]] == char:
            stac.pop()

    rev = reversed(stac)

    for char in rev:
        val = rever[char]
        score = score * 5
        if val == ')':
            score = score + 1
        if val == ']':
            score = score + 2
        if val == '}':
            score = score + 3
        if val == '>':
            score = score + 4

    score_list.append(score)

sored_scores = sorted(score_list)


index_middle = (len(sored_scores) // 2)

print(sored_scores[index_middle])