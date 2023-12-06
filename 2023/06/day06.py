from math import sqrt, ceil, floor

day = "06"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

times = []
distances = []
winning = {i : [] for i in range(1, 5)}

with open(file) as f:
    input = f.readlines()
    times = input[0].split(":")[1].split()
    distances = input[1].split(":")[1].split()

races = list(zip(times, distances))
races = [ (int(i[0]), int(i[1])) for i in races ]

def getDistance(button, time):
    dist = (time - button) * button
    return dist

i = 0
for race in races:
   i += 1
   for b in range(0, race[0]):
       if getDistance(b, race[0]) > race[1]:
           winning[i].append(b)    

result = 1
for r in winning:
    if len(winning[r]) > 0: 
        result *= len(winning[r])

print(result)

# PART 2
time2 = ""
distance2 = ""
result = 0
for race in races:
    time2 += str(race[0])
    distance2 += str(race[1])

time2 = int(time2)
distance2 = int(distance2)

lowEnd = (-time2 + sqrt(time2**2 + 4 * - distance2)) / -2
highEnd = (-time2 - sqrt(time2**2 + 4 * -distance2)) / -2

lowEnd = ceil(lowEnd)
highEnd = floor(highEnd)


result = highEnd - lowEnd + 1
print('------------------')
print(result)