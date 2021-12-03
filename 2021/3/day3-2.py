source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/3/" + source + ".txt"

with open(file, 'r') as f:
  list = f.read().splitlines()

oxylist = list.copy()

for p in range(len(oxylist[1])):
    one = 0
    null = 0
    for i in range(len(oxylist)):
        m = [*map(int,str(oxylist[i]))]
        if m[p] == 1:
            one = one + 1
        elif m[p] == 0:
            null = null + 1
    r = []
    if one < null:
        for j in range(len(oxylist)):
            n = [*map(int,str(oxylist[j]))]
            if n[p] == 1:
                r.append(oxylist[j])
        for k in range(len(r)):
            oxylist.remove(r[k])
    else:
        for j in range(len(oxylist)):
            n = [*map(int,str(oxylist[j]))]
            if n[p] == 0:
                r.append(oxylist[j])
        for k in range(len(r)):
            oxylist.remove(r[k])
    if len(oxylist) == 1:
            break

oxy = int(oxylist[0], 2)

print(oxy)

scrubberlist = list.copy()

for p in range(len(scrubberlist[1])):
    one = 0
    null = 0
    for i in range(len(scrubberlist)):
        m = [*map(int,str(scrubberlist[i]))]
        if m[p] == 1:
            one = one + 1
        elif m[p] == 0:
            null = null + 1
    r = []
    if one < null:
        for j in range(len(scrubberlist)):
            n = [*map(int,str(scrubberlist[j]))]
            if n[p] == 0:
                r.append(scrubberlist[j])
        for k in range(len(r)):
            scrubberlist.remove(r[k])
    else:
        for j in range(len(scrubberlist)):
            n = [*map(int,str(scrubberlist[j]))]
            if n[p] == 1:
                r.append(scrubberlist[j])
        for k in range(len(r)):
            scrubberlist.remove(r[k])
    if len(scrubberlist) == 1:
            break

scrubber = int(scrubberlist[0], 2)

print(scrubber)
print(oxy * scrubber)