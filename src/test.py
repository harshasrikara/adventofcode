def constructSequence(num, lowerEnd, upperEnd):
    if ((upperEnd - lowerEnd)*2 < num):
        return [-1]
    ll = []
    if (num <= upperEnd - lowerEnd + 2):
        ll.append(upperEnd - 1)
        leng = 1
        ptr = 0
        while (leng < num):
            ll.append(upperEnd - ptr)
            leng = leng + 1
            ptr = ptr + 1
        return ll
    excess = num - (upperEnd - lowerEnd + 1)
    for i in range(excess):
        ll.append(upperEnd - excess)
        excess = excess - 1
    ptr = 0
    for i in range(upperEnd - lowerEnd + 1):
        ll.append(upperEnd - ptr)
        ptr = ptr + 1
    return ll


print(constructSequence(10, 4, 11))
