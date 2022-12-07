import re

day = "07"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

with open(file) as file:
    input = file.read().splitlines()

counter = 0
currentPath = []
pathsObject = {}

for line in input:
    command = line.split(" ")
    if command[1] == "cd":
        if command[2] == "..":
            currentPath.pop()
        else:
            currentPath.append(command[2])
    elif command[1] == "ls":
        continue
    elif command[0] == "dir":
        continue
    else:
        size = int(command[0])
        for p in range(len(currentPath) + 1):
            sep = "/"
            path = sep.join(currentPath[0:p])
            if path in pathsObject:
                pathsObject[path] += size
            else:
                pathsObject[path] = size

print(pathsObject)

partOne = 0

for p in pathsObject:
    if pathsObject[p] < 100000:
        partOne += pathsObject[p]

print(partOne)

total = 70000000
needed = 30000000
currentFree = total - pathsObject["/"]
currentNeeded = needed - currentFree
currentDir = total

for p in pathsObject:
    if pathsObject[p] > currentNeeded:
        if pathsObject[p] < currentDir:
            currentDir = pathsObject[p]

partTwo = currentDir
print(currentDir)