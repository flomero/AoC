from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt

day = "10"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"
with open(file, 'r') as f:
  input = f.read().splitlines()

x = 1
cycle = 0
strengths = []

def checkCycle(cycle):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return True


for line in input:
    line = line.split(" ")
    if line[0] == "noop":
        cycle += 1
        if checkCycle(cycle):
            strengths.append(cycle * x)
    else:
        value = int(line[1])
        cycle += 1
        if checkCycle(cycle):
            strengths.append(cycle * x)
        cycle += 1
        if checkCycle(cycle):
            strengths.append(cycle * x)
        x += value

print(sum(strengths))

cycle = 0
x = 1

row = np.array([0 for _ in range(40)])
image = np.tile(row, (6, 1))

def draw():
    global cycle
    global image
    global x
    pos = (cycle % 40) - 1
    row = cycle // 40
    if pos in [x-1, x, x+1]:
        image[row][pos] = 1

for line in input:
    line = line.split(" ")
    if line[0] == "noop":
        cycle += 1
        draw()
    else:
        value = int(line[1])
        cycle += 1
        draw()
        cycle += 1
        draw()
        x += value

image = np.delete(image, -1, axis=1)

plt.imshow(image, cmap="Blues")
plt.axis('off')
plt.savefig("C:/Users/flofi/repos/CodeImAdvent/2022/10/image.png", bbox_inches='tight', pad_inches=0.0)
plt.show()
