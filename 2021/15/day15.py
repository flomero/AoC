import numpy as np
import networkx as nx

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/15/" + source + ".txt"
input = np.genfromtxt(file, delimiter = 1, dtype=int)

def solve(arr):
    G = nx.grid_2d_graph(*arr.shape, create_using=nx.DiGraph)
    for _, i, j in G.edges(data=True):
        j["weight"] = arr[i]

    print(G)

    source, *_, target = G.nodes

    length = nx.shortest_path_length(G, source, target, weight="weight")
    return length

print(solve(input))

input2 = input
for i in range(4):
    input2 = np.concatenate((input2, np.add(input, i + 1)), axis = 1)
input3 = input2
for i in range(4):
    input3 = np.concatenate((input3, np.add(input2, i + 1)))
input3[input3 > 9] -= 9

print(solve(input3))