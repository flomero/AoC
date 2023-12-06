import re
import pprint
import numpy as np
import collections 

day = "05"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"
part = 2

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


            
if part == 1:
    for seed in seeds:
        seedDetails[seed] = [int(seed)]
        for map in maps:
            match = False
            for line in maps[map]:
                sourceStart = int(line[1])
                destStart = int(line[0])
                rangeLength = int(line[2])
                if sourceStart <= seedDetails[seed][-1] < sourceStart + rangeLength:
                    length = seedDetails[seed][-1] - sourceStart 
                    #print(str(seedDetails[seed][-1]) + " - " + str(length) + " - " + str(destStart) + " - " + str(destStart + length))
                    dest = destStart + length
                    seedDetails[seed].append(dest)
                    match = True
                    break
            if not match:
                seedDetails[seed].append(int(seedDetails[seed][-1]))

result = float("inf")
result2 = 0

for seed in seedDetails:
    if seedDetails[seed][-1] < result:
        result = seedDetails[seed][-1]


reversedMap = collections.OrderedDict(reversed(list(maps.items())))
print(reversedMap)


if part == 2: 
    pairs = list(zip(seeds, seeds[1:]))
    del pairs[1::2]    
    # find min pair[0] 
    # min = 10000000000
    #for pair in pairs:
    #    if int(pair[0]) < min:
    #        min = int(pair[0])
    # print(min)
    # sort pairs by pair[0] reverse
    pairs = sorted(pairs, key=lambda x: int(x[0]))

    for i in range(0, 1000000000):
        currentValue = i
        print(i)
        values = []
        for map in reversedMap:
            match = False
            for line in reversedMap[map]:
                sourceStart = int(line[1])
                destStart = int(line[0])
                rangeLength = int(line[2])
                if destStart <= currentValue < destStart + rangeLength:
                    length = currentValue - destStart 
                    dest = sourceStart + length
                    currentValue = dest
                    values.append(dest)
                    match = True
                    break
            if not match:
                values.append(currentValue)
        print(values)
        #print(currentValue)


        for pair in pairs:
            minP = int(pair[0])
            maxP = int(pair[0]) + int(pair[1])
            #print(minP , currentValue , maxP)
            if minP <= currentValue <= maxP:
                result2 = i
                break
        if result2 != 0:
            break



                
            


#pprint.pprint(maps)
#pprint.pprint(seedDetails)
print(result)	
print(result2)

    