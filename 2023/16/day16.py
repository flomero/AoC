import numpy as np

day = "16"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

input = np.genfromtxt(file, delimiter=1, dtype=str, comments=None)

# print(input)
tiles = {
    ".": {
        "ft": [(1, 0)],
        "fl": [(0, 1)],
        "fr": [(0, -1)],
        "fb": [(-1, 0)], 
    },
    "|": {
        "ft": [(1, 0)],
        "fl": [(-1, 0), (1, 0)],
        "fr": [(-1, 0), (1, 0)],
        "fb": [(-1, 0)], 
    },
    "-": {
        "ft": [(0, 1), (0, -1)],
        "fl": [(0, 1)],
        "fr": [(0, -1)],
        "fb": [(0, -1), (0, 1)], 
    },
    "/": {
        "ft": [(0, -1)],
        "fl": [(1, 0)],
        "fr": [(-1, 0)],
        "fb": [(0, 1)], 
    },
    "\\": {
        "ft": [(0, 1)],
        "fl": [(-1, 0)],
        "fr": [(1, 0)],
        "fb": [(0, -1)], 
    },
}

directions = {
    (1, 0): "ft",
    (0, 1): "fl",
    (0, -1): "fr",
    (-1, 0): "fb",
}

currentDir = (0, 1)
currentTile = (0, 0)


def getPath(currentTile, currentDir):
    newDirs = tiles[input[currentTile]][directions[currentDir]]
    print(newDirs)
    for newDir in newDirs:
        currentDir = newDir
        newTile = (currentTile[0] + currentDir[0], currentTile[1] + currentDir[1])
        getPath(newTile, currentDir)
        input[currentTile] = "X"
# rewrite with while loop
def newGetPath(currentTile, currentDir):
    while True:
        newDirs = tiles[input[currentTile]][directions[currentDir]]
        print(newDirs)
        for newDir in newDirs:
            currentDir = newDir
            newTile = (currentTile[0] + currentDir[0], currentTile[1] + currentDir[1])
            getPath(newTile, currentDir)
            input[currentTile] = "X"
        if input[currentTile] == "X":
            break
    return input


newGetPath(currentTile, currentDir)
print(input)
