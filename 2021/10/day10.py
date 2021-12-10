source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/10/" + source + ".txt"

with open(file, 'r') as f:
  input = f.read().splitlines()

stops = []
pairs = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
}

points = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

for i in input:
    current = []
    for x in i:
        if x in pairs.keys():
            if len(current) == 0:
                stops.append(x)
                break
            last = current.pop()
            if last != pairs[x]:
                stops.append(x)
                break
        else:
            current.append(x)

print(stops)

result = 0
for s in stops:
    result = result + points[s]

print(result)