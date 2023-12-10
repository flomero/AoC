day = "09"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

histories = []
result = 0

with open(file) as f:
    for line in f:
        line = [int(n) for n in line.strip().split()]
        histories.append(line)


for history in histories:
    print(history)
    steps = [history]
    while True: 
        newline = []
        for i in range(len(steps[-1])- 1):
            x = abs(steps[-1][i] - steps[-1][i+1])
            newline.append(x)
        steps.append(newline)
        if newline.count(0) == len(newline):
            break
    print(steps)
    # reverse steps
    steps = steps[::-1]
    for index, step in enumerate(steps):
        if index == len(steps) - 1:
            result += steps[-1][-1]
            break
        if len(step) == 0:
            step.append(0)
        x = step[-1] + steps[index + 1][-1]
        steps[index + 1].append(x)

    print(steps)


print(result)
