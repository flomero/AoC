import numpy as np

day = "17"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

input = np.genfromtxt(file, delimiter=1, dtype=int)
limit = 3
start = (0, 0)
end = (len(input[0])-1, len(input)-1)

result = 0

unvisited = set()
for x in range(len(input)):
    for y in range(len(input[0])):
        unvisited.add((x, y))

visited = {i : np.inf for i in unvisited}

visited[start] = 0

def get_neighbours(pos):
    neighbours = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            neighbours.append((pos[0]+x, pos[1]+y))
    return neighbours

while len(unvisited) > 0:
    i = unvisited.pop()
    neighbours = get_neighbours(i)
    for n in neighbours:
        if n[0] < 0 or n[1] < 0 or n[0] > end[0] or n[1] > end[1]:
            continue
        if visited[n] < np.inf:
            visited[i] = visited[n] + input[i[1]][i[0]]
            
            break

print(visited)

print(visited[end])

