import numpy as np
import matplotlib.pyplot as plt

day = "08"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"
input = np.genfromtxt(file, delimiter = 1, dtype=int, unpack=False)

map = []
for i in range(len(input)):
    map.append([])
    for j in range(len(input[i])):
        map[i].append(0)

mapX = np.array(map)
mapY = np.rot90(np.array(map))
inputRot = np.rot90(input)

def generateMaps(start, end):
    for i, line in enumerate(start):
        if i == 0 or i == (len(start) - 1):
            for j in range(len(end[0])):
                end[i][j] = 1
        else:
            l = len(line)
            for j in range(l):
                if j == 0 or j == (len(line) - 1):
                    end[i][j] = 1
                elif line[j] > np.max(line[0:j]):
                    end[i][j] = 1
                elif line[j] > np.max(line[(j+1):l]):
                    end[i][j] = 1


generateMaps(input, mapX)
generateMaps(inputRot, mapY)

mapY = np.rot90(mapY, 3)
mapResult = mapX + mapY

partOne = np.count_nonzero(mapResult)
print(partOne)


 

scenicScore = 0
scenicMapX = np.array(map)
scenicMapY = np.rot90(np.array(map))

def generateScore(start, end):
    for i, line in enumerate(start):
        if i == 0 or i == (len(start) - 1):
            for j in range(len(end[0])):
                end[i][j] = 0
        else:
            l = len(line)
            for j in range(l):
                a = 0
                b = 0
                left = []
                right = []
                if j == 0 or j == (len(line) - 1):
                    end[i][j] = 0
                else:
                    for s in range(j):
                        left.append(line[j-s-1]) 
                    for s in range(len(line) - j -1):
                        right.append(line[j+s+1]) 
                for  l in left:
                    if l < line[j]:
                        a += 1
                    else:
                        a += 1 
                        break 
                for r in right:
                    if r < line[j]:
                        b += 1
                    else:
                        b += 1
                        break
                end[i][j] = a * b
                        

generateScore(input, scenicMapX)
generateScore(inputRot, scenicMapY)
scenicMapY = np.rot90(scenicMapY, 3)

scenicMap = np.multiply(scenicMapX, scenicMapY)

partTwo = np.max(scenicMap)
print(partTwo)

def highlight_cell(x,y, ax=None, **kwargs):
    rect = plt.Rectangle((x-.5, y-.5), 1,1, fill=False, **kwargs)
    ax = ax or plt.gca()
    ax.add_patch(rect)
    return rect
 
for i in range(len(mapResult)):
    for j in range(len(mapResult[i])):
        if int(mapResult[i][j]) > 0:
            highlight_cell(i,j, color="black", linewidth=0.5)

[x,y] = np.where(scenicMap == partTwo)
highlight_cell(x, y, color="r", linewidth=1)

plt.imshow(input, cmap="Greens")
plt.axis('off')
plt.savefig("C:/Users/flofi/repos/CodeImAdvent/2022/08/forest.svg", bbox_inches='tight', pad_inches=0.0)
plt.show()
