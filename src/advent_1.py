
file1 = open('../res/advent_1.txt', 'r')
Lines = file1.readlines() 

ll = []
copy_list = []
nex = []

for line in Lines:
    ll.append(line)
    copy_list.append(line)
    nex.append(line)

ll = list(map(lambda x: int(x), ll))
copy_list = list(map(lambda x: int(x), copy_list))
nex = list(map(lambda x: int(x), nex))

for entry in ll:
    for ent in copy_list:
        for val in nex:
        # print(str(entry) +  " " + str(ent)) 
            if(entry + ent + val == 2020):
                print(entry)
                print(ent)
                print(entry*ent*val)
        # print(entry)
        # print(ent)