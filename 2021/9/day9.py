import numpy as np

source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/9/" + source + ".txt"
input = np.genfromtxt(file, delimiter = 1, dtype=int)

def find_neighbors(arr, i, j):
    neighbors = []
    if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
        if i != 0:
            neighbors.append(arr[i-1][j])
        if j != len(arr[i]) - 1:
            neighbors.append(arr[i][j+1])
        if i != len(arr) - 1:
            neighbors.append(arr[i+1][j])
        if j != 0:
            neighbors.append(arr[i][j-1])
    else:
        neighbors = [
            arr[i - 1][j],  
            arr[i][j + 1],
            arr[i + 1][j],
            arr[i][j - 1]
        ]
    return neighbors

lows = []

for i in range(len(input)):
    for j, v in enumerate(input[i]):
        n = find_neighbors(input, i, j)
        if input[i][j] < np.amin(n):
            lows.append(input[i][j])

output = np.sum(lows) + len(lows)
print(output)

def find_basins(arr, i, j):
    if 0 <= i < len(arr) and 0 <= j < len(arr[i]) and arr[i][j] != 9:
        arr[i][j] = 9
        return(
            1
            + find_basins(arr, i + 1, j)
            + find_basins(arr, i, j + 1)
            + find_basins(arr, i - 1, j)
            + find_basins(arr, i, j - 1)
        )
    return 0

basins = []

for i in range(len(input)):
    for j, v in enumerate(input[i]):
        basins.append(find_basins(input, i, j))

highest = sorted(basins, reverse=True)
print(highest[0] * highest[1] * highest[2])