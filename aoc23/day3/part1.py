import sys

size = 140

def printMatrix(matrix) -> None:
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            print(matrix[x][y], end="")
        print()

def buildMatrix(file) -> list[list[str]]:
    m = [[0 for x in range(size)] for y in range(size)] 

    y = 0
    for line in file.readlines():
        line = line.strip('\n')
        print(line)

        for x in range(0, len(line)):
            m[x][y] = line[x]
        
        y = y + 1
    
    return m

def getFullNumber(matrix: list[list[str]], x: int, y: int) -> [int, int]:
    if not matrix[x][y].isdigit():
        raise Exception()

    number = ""
    while x >= 0 and matrix[x][y].isdigit():
        x = x - 1

    if not matrix[x][y].isdigit():
        x = x + 1
    
    while x < size and matrix[x][y].isdigit():
        number = number + matrix[x][y]
        x = x + 1

    return int(number), len(number)

def hasSpecialCharacter(matrix: list[list[str]], x: int, y: int) -> bool:
    skipTop, skipBottom, skipLeft, skipRight = False, False, False, False
    if x == 0:
        skipLeft = True
    if x == size - 1:
        skipRight = True
    if y == 0:
        skipTop = True
    if y == size - 1:
        skipBottom = True

    specialCharacter = False

    if not skipRight:
        if matrix[x+1][y] != "." and not matrix[x+1][y].isdigit():
            specialCharacter = True
    if not skipRight and not skipBottom:
        if matrix[x+1][y+1] != "." and not matrix[x+1][y+1].isdigit():
            specialCharacter = True
    if not skipBottom:
        if matrix[x][y+1] != "." and not matrix[x][y+1].isdigit():
            specialCharacter = True
    if not skipLeft and not skipBottom:
        if matrix[x-1][y+1] != "." and not matrix[x-1][y+1].isdigit():
            specialCharacter = True
    if not skipLeft:
        if matrix[x-1][y] != "." and not matrix[x-1][y].isdigit():
            specialCharacter = True
    if not skipLeft and not skipTop:
        if matrix[x-1][y-1] != "." and not matrix[x-1][y-1].isdigit():
            specialCharacter = True
    if not skipTop:
        if matrix[x][y-1] != "." and not matrix[x][y-1].isdigit():
            specialCharacter = True
    if not skipRight and not skipTop:
        if matrix[x+1][y-1] != "." and not matrix[x+1][y-1].isdigit():
            specialCharacter = True

    return specialCharacter
    
def isGear(matrix: list[list[str]], x: int, y: int) -> [bool, int]:
    skipTop, skipBottom, skipLeft, skipRight = False, False, False, False
    if x == 0:
        skipLeft = True
    if x == size - 1:
        skipRight = True
    if y == 0:
        skipTop = True
    if y == size - 1:
        skipBottom = True

    surroundingNumbers = 0
    numbers = []

    if not skipRight:
        if matrix[x+1][y].isdigit():
            surroundingNumbers = surroundingNumbers + 1
            number, length = getFullNumber(matrix, x+1, y)
            numbers.append(number)
    if not skipRight and not skipBottom:
        if matrix[x+1][y+1].isdigit():
            surroundingNumbers = surroundingNumbers + 1
            number, length = getFullNumber(matrix, x+1, y+1)
            numbers.append(number)
    if not skipBottom:
        if matrix[x][y+1].isdigit():
            surroundingNumbers = surroundingNumbers + 1
            number, length = getFullNumber(matrix, x, y+1)
            numbers.append(number)
    if not skipLeft and not skipBottom:
        if matrix[x-1][y+1].isdigit():
            surroundingNumbers = surroundingNumbers + 1
            number, length = getFullNumber(matrix, x-1, y+1)
            numbers.append(number)
    if not skipLeft:
        if matrix[x-1][y].isdigit():
            surroundingNumbers = surroundingNumbers + 1
            number, length = getFullNumber(matrix, x-1, y)
            numbers.append(number)
    if not skipLeft and not skipTop:
        if matrix[x-1][y-1].isdigit():
            surroundingNumbers = surroundingNumbers + 1
            number, length = getFullNumber(matrix, x-1, y-1)
            numbers.append(number)
    if not skipTop:
        if matrix[x][y-1].isdigit():
            surroundingNumbers = surroundingNumbers + 1
            number, length = getFullNumber(matrix, x, y-1)
            numbers.append(number)
    if not skipRight and not skipTop:
        if matrix[x+1][y-1].isdigit():
            surroundingNumbers = surroundingNumbers + 1
            number, length = getFullNumber(matrix, x+1, y-1)
            numbers.append(number)

    numbers = list(set(numbers))

    print("new entry")
    print([x, y])
    print(surroundingNumbers)
    print(numbers)

    if len(numbers) > 1:
        return True, numbers[0]*numbers[1]
    else:
        return False, 0

def getPartNumbers(matrix) -> int:
    x, y = 0, 0
    sum = 0

    while y < size:
        while x < size:

            if matrix[x][y].isdigit():
                number, length = getFullNumber(matrix, x, y)

                partNum = False
                for i in range(length):
                    partNum = partNum or hasSpecialCharacter(matrix, x + i, y)
                
                if partNum:
                    sum = sum + number
                
                x = x + length - 1
            
            x = x + 1
        
        x = 0
        y = y + 1

    return sum

def getGearRatios(matrix) -> int:
    x, y = 0, 0
    sum = 0

    while y < size:
        while x < size:
            if matrix[x][y] == '*':
                gear, ratio = isGear(matrix, x, y)

                if gear:
                    sum = sum + ratio
                
            x = x + 1
        
        x = 0
        y = y + 1
    
    return sum

def main() -> int:
    f = open("/Users/harshasrikara/aoc23/day3/input.txt")

    m = buildMatrix(f)

    printMatrix(m)

    print(getGearRatios(m))

    return 0


if __name__ == '__main__':
    sys.exit(main()) 