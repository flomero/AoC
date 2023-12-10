import re
import matplotlib.pyplot as plt

day = "10"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

startChar = "S"
start = (0, 0)
dirs = {
    "|": {"ft": (1, 0), "fb": (-1, 0)},
    "-": {"fl": (0, 1), "fr": (0, -1)},
    "L": {"ft": (0, 1), "fr": (-1, 0)},
    "7": {"fb": (0, -1), "fl": (1, 0)},
    "J": {"ft": (0, -1), "fl": (-1, 0)},
    "F": {"fb": (0, 1), "fr": (1, 0)}
}
fromDir = {
    (1, 0): "ft",
    (-1, 0): "fb",
    (0, 1): "fl",
    (0, -1): "fr",
    (0, 0): "start"
}

input = []
with open(file) as f:
    for line in f:
        input.append(line.strip())

def findStart(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == startChar:
                return (i, j)
    return (0, 0)

start = findStart(input)

x = 0
visited = [start]
next = (0, 0)
lastStep = (0, 0)

if input[start[0]][start[1] + 1] == "-" or input[start[0]][start[1] + 1] == "7" or input[start[0]][start[1] + 1] == "J":
    next = (start[0], start[1] + 1)
    lastStep = (0, 1)
elif input[start[0] + 1][start[1]] == "|" or input[start[0] + 1][start[1]] == "L" or input[start[0] + 1][start[1]] == "7":
    next = (start[0] + 1, start[1])
    lastStep = (1, 0)
elif input[start[0] - 1][start[1]] == "|" or input[start[0] - 1][start[1]] == "F" or input[start[0] - 1][start[1]] == "J":
    next = (start[0] - 1, start[1])
    lastStep = (-1, 0)
elif input[start[0]][start[1] - 1] == "-" or input[start[0]][start[1] - 1] == "L" or input[start[0]][start[1] - 1] == "F":
    next = (start[0], start[1] - 1)
    lastStep = (0, -1)

lastStep2 = lastStep

while True:
    #print(input[next[0]][next[1]])
    direction = fromDir[lastStep]
    if input[next[0]][next[1]] == startChar:
        break
    current = input[next[0]][next[1]]
    lastStep = dirs[current][direction]
    visited.append(next)
    x += 1
    next = (next[0] + lastStep[0], next[1] + lastStep[1])
    #print(next)

result = int((x + 1) / 2)
print(result)

# Part 2

result = 0
maxlen = 0

for i in range(len(input)):
    # add "." between each char
    input[i] = ".".join(input[i])
    input[i] = re.sub(r"\-\.", "--", input[i])
    input[i] = re.sub(r"L\.", "L-", input[i])
    input[i] = re.sub(r"F\.", "F-", input[i])
    if len(input[i]) > maxlen:
        maxlen = len(input[i])


zoomedOut = []

# add lines between each line
for i in range(len(input) * 2 - 1):
    if i % 2 == 0:
        zoomedOut.append(input[int(i / 2)])
    else:
        zoomedOut.append("." * maxlen)	

for i in range(len(zoomedOut) - 2):
    if i % 2 != 0:
        continue
    for j in range(len(zoomedOut[i])):
        if zoomedOut[i][j] == "S" and zoomedOut[i + 2][j] in ["|", "J", "L"]:
            zoomedOut[i+1] = zoomedOut[i+1][:j] + "|" + zoomedOut[i+1][j+1:] 
        elif zoomedOut[i][j] == "7" and zoomedOut[i + 2][j] in ["|", "J", "L", "S"]:
            zoomedOut[i+1] = zoomedOut[i+1][:j] + "|" + zoomedOut[i+1][j+1:]
        elif zoomedOut[i][j] == "F" and zoomedOut[i + 2][j] in ["|", "J", "L", "S"]:
            zoomedOut[i+1] = zoomedOut[i+1][:j] + "|" + zoomedOut[i+1][j+1:]
        elif zoomedOut[i][j] == "|":
            zoomedOut[i+1] = zoomedOut[i+1][:j] + "|" + zoomedOut[i+1][j+1:]
            

for i in range(len(zoomedOut)):
    print(zoomedOut[i])

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == startChar:
            start = (i, j)
            break

input = zoomedOut
start = findStart(input)

x = 0
visited = [start]
lastStep = lastStep2
next = (start[0] + lastStep[0], start[1] + lastStep[1])

print(start)
print(lastStep)
print(next)

while True:
    #print(input[next[0]][next[1]])
    direction = fromDir[lastStep]
    if input[next[0]][next[1]] == startChar:
        break
    current = input[next[0]][next[1]]
    lastStep = dirs[current][direction]
    visited.append(next)
    x += 1
    next = (next[0] + lastStep[0], next[1] + lastStep[1])
    #print(next)

for v in visited:
    input[v[0]] = input[v[0]][:v[1]] + "#" + input[v[0]][v[1]+1:]

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != "#":
            input[i] = input[i][:j] + "." + input[i][j+1:]	

input.insert(0, "." * len(input[0]))
input.append("." * len(input[0]))
for i in range(len(input)):
    input[i] = "." + input[i] + "."

for i in range(len(input)):
    print(input[i])


def floodfill(x, y, input):
    next = [(x, y)]
    while True:
        new = []
        if len(next) == 0:
            break
        for n in next:

            x = n[0]
            y = n[1]
            print(x, y)
            if x < 0 or y < 0 or x >= len(input) or y >= len(input[x]):
                continue
            if input[x][y] == ".":
                input[x] = input[x][:y] + " " + input[x][y+1:]
                if x + 1 < len(input) and input[x + 1][y] == ".":
                    new.append((x + 1, y))
                if x - 1 >= 0 and input[x - 1][y] == ".":
                    new.append((x - 1, y))
                if y + 1 < len(input[x]) and input[x][y + 1] == ".":
                    new.append((x, y + 1))
                if y - 1 >= 0 and input[x][y - 1] == ".":
                    new.append((x, y - 1))
                next = new
            else:
                continue

floodfill(0, 0, input)

input = input[1:-1]
for i in range(len(input)):
    input[i] = input[i][1:-1]

input = input[::2]
for i in range(len(input)):
    input[i] = input[i][::2]

for i in range(len(input)):
    print(input[i])
    for j in range(len(input[i])):
        if input[i][j] == ".":
            result += 1

print(result)

# Plot

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            input[i] = input[i][:j] + "5" + input[i][j+1:]
        elif input[i][j] == " ":
            input[i] = input[i][:j] + "0" + input[i][j+1:]
        else:
            input[i] = input[i][:j] + "1" + input[i][j+1:]
    input[i] = list(input[i])
    input[i] = list(map(int, input[i]))



plt.imshow(input, interpolation='none')
# no axis
plt.axis('off')
plt.savefig("C:/Users/flofi/repos/CodeImAdvent/2023/10/loop.svg", bbox_inches='tight', pad_inches=0.0)
plt.show()

