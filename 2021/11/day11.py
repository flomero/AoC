import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/11/" + source + ".txt"
input = np.genfromtxt(file, delimiter = 1, dtype=int)

fig = plt.gcf()
im = plt.imshow(input)

steps = 1000
f = steps

def addns(arr, i, j):
    if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
        if i != 0:
            arr[i - 1][j] = arr[i - 1][j] + 1
        if j != len(arr[i]) - 1:
            arr[i][j + 1] = arr[i][j + 1] + 1
        if i != len(arr) - 1:
            arr[i + 1][j] = arr[i + 1][j] + 1
        if j != 0:
            arr[i][j - 1] = arr[i][j - 1] + 1
        if i != 0 and j != 0:
            arr[i - 1][j - 1] = arr[i - 1][j - 1] + 1
        if i != 0 and j != len(arr[i]) - 1:
            arr[i - 1][j + 1] = arr[i - 1][j + 1] + 1
        if i != len(arr) - 1 and j != 0:
            arr[i + 1][j - 1] = arr[i + 1][j - 1] + 1
        if i != len(arr) - 1 and j != len(arr[i]) - 1:
            arr[i + 1][j + 1] = arr[i + 1][j + 1] + 1
    else:
        arr[i][j + 1] = arr[i][j + 1] + 1
        arr[i][j - 1] = arr[i][j - 1] + 1
        arr[i + 1][j] = arr[i + 1][j] + 1
        arr[i - 1][j] = arr[i - 1][j] + 1
        arr[i + 1][j + 1] = arr[i + 1][j + 1] + 1
        arr[i + 1][j - 1] = arr[i + 1][j - 1] + 1
        arr[i - 1][j + 1] = arr[i - 1][j + 1] + 1
        arr[i - 1][j - 1] = arr[i - 1][j - 1] + 1
    return

blinks = 0
all = [input]

for s in range(steps):
    input = np.add(input, 1)
    blinked = []
    while np.asarray(np.where(input > 9)).size > 0:
        for i in range(len(input)):
            for j, v in enumerate(input[i]):
                if input[i][j] > 9:
                    if [i,j] not in blinked:
                        addns(input, i, j)
                        blinked.append([i,j])
                        for b in blinked:
                            input[b[0]][b[1]] = 0
                    else:
                       for b in blinked:
                            input[b[0]][b[1]] = 0 
    blinks = blinks + len(blinked)
    all.append([input])
    if len(blinked) == 100:
        print(s + 1)
        f = s
        all.append([input])
        break

def animate(frame):
    this = all[frame]
    print(this)
    this =np.squeeze(this)
    im = plt.imshow(this)
    return im

anim = FuncAnimation(fig, animate, frames = f, interval = 50)
anim.save("C:/Users/flofi/repos/CodeImAdvent/2021/11/animation.gif")
print(input)
print(blinks)
