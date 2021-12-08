import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/8/" + source + ".txt"
input = np.loadtxt(file, delimiter="\n", dtype=str)

output = 0

for i in input:
    add = ""
    split1 = i.split(" | ")
    string1 = ""
    for s in split1[0]:
        string1 = string1 + s 
    split2 = string1.split(" ")
    for s in split2:
        if len(s) == 2:
            one = s
        elif len(s) == 3:
            seven = s
        elif len(s) == 4:
            four = s
        elif len(s) == 7:
            eight = s

    string3 = ""
    for s in split1[1]:
        string3 = string3 + s 
    split3 = string3.split(" ")
    for s in split3:
        if len(s) == 2:
            add = add + "1"
        elif len(s) == 3:
            add = add + "7"
        elif len(s) == 4:
            add = add + "4"
        elif len(s) == 7:
            add = add + "8"
        elif len(s) == 5:
            a1 = list(s)
            a2 = list(one)
            a3 = list(four)
            dif1 = list(set(a1) - set(a2))
            dif2 = list(set(a1) - set(a3))
            if len(dif1) == 3:
                add = add + "3"
            elif len(dif2) == 2:
                add = add + "5"
            else:
                add = add + "2"
        elif len(s) == 6:
            a1 = list(s)
            a2 = list(one)
            a3 = list(four)
            dif1 = list(set(a1) - set(a2))
            dif2 = list(set(a1) - set(a3))
            if len(dif1) == 5:
                add = add + "6"
            elif len(dif2) == 3:
                add = add + "0"
            else:
                add = add + "9"
    output = output + int(add)
    print(add)

print(output)


    
