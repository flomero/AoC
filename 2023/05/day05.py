import re
import pprint
import numpy as np
import collections 

day = "05"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

seeds = []
seedDetails = {}

maps = collections.OrderedDict({
    "seed-to-soil" : [] ,
    "soil-to-fertilizer" : [],
    "fertilizer-to-water" : [],
    "water-to-light" : [],
    "light-to-temperature" : [],
    "temperature-to-humidity"  : [],
    "humidity-to-location" : []
})

with open(file) as f:
    content = f.readlines()
    seeds = content[0].split(":")[1].strip().split(" ")
    currentMap = ""        
    for line in content[1:]:
        if any(map in line for map in maps):
            currentMap = next(map for map in maps if map in line)
            continue
        if line == "\n":
            currentMap = ""
            continue
        if currentMap != "":
            maps[currentMap].append(line.strip().split())

for seed in seeds:
    seedDetails[seed] = [int(seed)]
    for map in maps:
        match = False
        for line in maps[map]:
            sourceStart = int(line[1])
            destStart = int(line[0])
            rangeLength = int(line[2])
            if sourceStart <= seedDetails[seed][-1] <= sourceStart + rangeLength:
                length = seedDetails[seed][-1] - sourceStart 
                print(str(seedDetails[seed][-1]) + " - " + str(length) + " - " + str(destStart) + " - " + str(destStart + length))
                dest = destStart + length
                seedDetails[seed].append(dest)
                match = True
        if not match:
            seedDetails[seed].append(int(seedDetails[seed][-1]))

result = float("inf")
for seed in seedDetails:
    if seedDetails[seed][-1] < result:
        result = seedDetails[seed][-1]
        
pprint.pprint(maps)

pprint.pprint(seedDetails)
print(result)

    