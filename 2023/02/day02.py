import re

day = "02"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

input = []
games = {}
result = 0

colors = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open(file, "r") as f:
    for line in f:
        input.append(line.strip())

for i in input:
    gameNumber = re.split(r' ', re.split(r':', i)[0])[1]
    games[gameNumber] = {}
    steps = re.split(r';', re.split(r':', i)[1])
    for index, step in enumerate(steps):
        games[gameNumber][index] = {}
        step = re.split(r',', step.strip())
        for s in step:
            s = re.split(r' ', s.strip())
            games[gameNumber][index][s[1]] = int(s[0]) + games[gameNumber][index].get(s[1], 0)

for game in games:
    valid = True
    for step in games[game]:
        for color in games[game][step]:
            if games[game][step][color] > colors[color]:
                valid = False
    if valid:
        result += int(game)    
            
print(games)
print(result)

# Part 2
gamePowers = {}
result2 = 0

for game in games:
    r = b = g = 0
    for step in games[game]:
        if games[game][step].get('red', 0) > r: r = games[game][step].get('red', 0)
        if games[game][step].get('blue', 0) > b: b = games[game][step].get('blue', 0)
        if games[game][step].get('green', 0) > g: g = games[game][step].get('green', 0)
    gamePowers[game] = r * b * g

for game in gamePowers:
    result2 += gamePowers[game]

print(gamePowers)
print(result2)

            