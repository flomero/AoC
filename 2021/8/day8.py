import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/8/" + source + ".txt"
input = np.loadtxt(file, delimiter="\n", dtype=str)

one = four = seven = eight = 0

for i in input:
    split1 = i.split(" | ")
    string1 = ""
    for s in split1[1]:
        string1 = string1 + s 
    split2 = string1.split(" ")
    for s in split2:
        if len(s) == 2:
            one = one + 1
        elif len(s) == 3:
                seven = seven + 1
        elif len(s) == 4:
                four = four + 1
        elif len(s) == 7:
                eight = eight + 1

result = one + four + seven + eight
print(result)