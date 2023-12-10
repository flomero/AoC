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

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == startChar:
            start = (i, j)
            break


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

while True:
    print(input[next[0]][next[1]])
    direction = fromDir[lastStep]
    if input[next[0]][next[1]] == startChar:
        break
    current = input[next[0]][next[1]]
    lastStep = dirs[current][direction]
    visited.append(next)
    x += 1
    next = (next[0] + lastStep[0], next[1] + lastStep[1])
    print(next)

result = int((x + 1) / 2)
print(result)

            
        

