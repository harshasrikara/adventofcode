import copy

file1 = open('../res/advent_6.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)


class Person:
    yes = []
    confirmed_yes = []
    first = True

    def __init__(self):
        self.yes = []
        self.confirmed_yes = []
        self.first = True

    def get_count(self) -> int:
        return len(self.yes)


person = Person()
total = 0

for row in rows:
    if row == "\n":
        total = total + person.get_count()
        print(person.yes)
        person = Person()
    else:
        if person.first:
            for char in row:
                if not char in person.yes and char != "\n":
                    person.yes.append(char)
            person.first = False
        else:
            person.confirmed_yes = copy.deepcopy(person.yes)
            for entry in person.yes:
                if not entry in row and entry != "\n":
                    person.confirmed_yes.remove(entry)
            person.yes = person.confirmed_yes

print("total: " + str(total))
