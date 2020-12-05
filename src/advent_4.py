import re

file1 = open('../res/advent_4.txt', 'r')
Lines = file1.readlines()

rows = []

for line in Lines:
    rows.append(line)


class Passport:
    passport = {}
    all_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')
    valid_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    eye_cols = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    def __init__(self):
        self.passport = {}

    def representsInt(self, s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
    
    def check_hgt(self, h) -> bool:
        if self.representsInt(h):
            return False
        last_chars = h[-2:]
        if last_chars == 'in':
            x = int(h[0:len(h)-2])
            if x >= 59 and x <= 76:
                return True
        if last_chars == 'cm':
            x = int(h[0:len(h)-2])
            if x >= 150 and x <= 193:
                return True
        return False
    
    def validate_passport(self) -> bool:
        for val in self.valid_keys:
            if val not in self.passport:
                return False
        return True
    
    def validate_fields(self) -> bool:
        byr = self.passport['byr']
        if self.representsInt(byr):
            byr = int(byr)
            if byr < 1920 or byr > 2002:
                return False
        iyr = self.passport['iyr']
        if self.representsInt(iyr):
            iyr = int(iyr)
            if iyr < 2010 or iyr > 2020:
                return False
        eyr = self.passport['eyr']
        if self.representsInt(eyr):
            eyr = int(eyr)
            if eyr < 2020 or eyr > 2030:
                return False
        if not self.check_hgt(self.passport['hgt']):
            return False
        if not re.match('#[0-9a-f]{6}', self.passport['hcl']):
            return False
        if not self.passport['ecl'] in self.eye_cols:
            return False
        if not self.representsInt(self.passport['pid']) or len(self.passport['pid']) != 9:
            return False
        return True

current = Passport()
valid_count = 0
total_count = 0

for row in rows:
    if row == "\n":
        if current.validate_passport():
            if current.validate_fields():
                print(current.passport)
                valid_count = valid_count + 1
        current = Passport()
        total_count = total_count + 1
        continue
    else:
        keyset = row.split(" ")
        for entry in keyset:
            keys = entry.split(":")
            current.passport[keys[0]] = keys[1].split("\n")[0]

print("valid count: " + str(valid_count))
print("total count: " + str(total_count))
