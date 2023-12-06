import re
import pprint
import numpy as np
import collections 

day = "05"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"
part = 2

input = ""
seeds = []
result = float("inf")


with open(file) as f:
    input = f.read()

input = input.split("\n\n")
seeds = input[0].split(":")[1].strip().split()
maps = []
for i in input[1:]:
    x = [list(map(int, l.split())) for l in i.split("\n")[1:]]
    maps.append(x)

ranges = []

for map in maps:
    ranges.append([])
    for line in map:
        ranges[-1].append([line[0], line[1], line[2]])


def findLocation(seed):
    path = [int(seed)]
    for map in ranges:
        match = False
        for line in map:
            #print(line)
            sourceStart = int(line[1])
            destStart = int(line[0])
            rangeLength = int(line[2])
            if sourceStart <= path[-1] < sourceStart + rangeLength:
                length = path[-1] - sourceStart 
                #print(str(seedDetails[seed][-1]) + " - " + str(length) + " - " + str(destStart) + " - " + str(destStart + length))
                dest = destStart + length
                path.append(dest)
                match = True
                break
        if not match:
            path.append(int(path[-1]))
    return path[-1]

mapMins = [[] for i in range(len(maps))]

for i in range(len(maps)):
    for range in ranges[i]:
        if 0 not in mapMins[i]:
            mapMins[i].append(0)
        mapMins[i].append(range[1])
        mapMins[i].append(range[1] + range[2])

mapMins = [list(set(mapMin)) for mapMin in mapMins]
mapMins = [sorted(mapMin) for mapMin in mapMins]

print(mapMins)


        










                
            
