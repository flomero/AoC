from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/13/" + source + ".txt"
input = np.genfromtxt(file, delimiter = ",", dtype=int)

if source == "test":
    instruction = ["y=7","x=5"]
else:
    instruction = ["x=655","y=447","x=327","y=223","x=163","y=111","x=81","y=55","x=40","y=27","y=13","y=6"]

xmax, ymax = input.max(axis = 0)
paper  = np.zeros((ymax + 1, xmax + 1))

for row in input:
    paper[row[1]][row[0]] = 1

# now paper is set up for folding

for i in instruction:
    ipair = i.split("=")
    if ipair[0] == "x":  
        papers = np.hsplit(paper, [int(ipair[1]), int(ipair[1]) + 1])  
        paper = papers[0] + (np.fliplr(papers[2]))
        print(paper)
        print(np.count_nonzero(paper))
    else:
        papers = np.split(paper, [int(ipair[1]), int(ipair[1]) + 1])  
        paper = papers[0] + np.flip(np.fliplr(papers[2]))
        print(paper)
        print(np.count_nonzero(paper))

cmap = ListedColormap(["black", "darkorange"])
paper = np.where(paper < 1, paper, 1)
print(paper)

plt.matshow(paper, cmap = cmap)
plt.savefig("C:/Users/flofi/repos/CodeImAdvent/2021/13/img.png", transparent=True)