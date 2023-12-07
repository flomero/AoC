import pprint
import collections


day = "07"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"
part = 2

input = {}
chars = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
if part == 2:
    chars = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

types = ["5", "4", "fh", "3", "tp", "op", "hc"]
sortedHands = collections.OrderedDict({i : [] for i in types})
winningHands = []

with open(file) as f:
    for l in f:
        l = l.strip().split()
        input[l[0]] = {"bid" : l[1]}

for hand in input.keys():
    print(hand)
    counts = {}
    for c in chars:
        counts[c] = hand.count(c)
    if part == 2:
        j = hand.count("J")
        if j > 0:
            highestCount = 0
            for c in counts:
                if c != "J" and counts[c] > highestCount:
                    highestCount = counts[c]
            highestCard = list(counts.keys())[list(counts.values()).index(highestCount)]
            counts[highestCard] += j
            counts["J"] = 0

    for c in counts:
        if counts[c] == 5:
            input[hand]["type"] = "5"
        elif counts[c] == 4:
            input[hand]["type"] = "4"
        elif counts[c] == 3:   
            if 2 in counts.values():
                input[hand]["type"] = "fh"
            else:
                input[hand]["type"] = "3"
        elif counts[c] == 2:
            if list(counts.values()).count(2) == 2:
                input[hand]["type"] = "tp"
            elif 3 in counts.values():
                input[hand]["type"] = "fh"
            else:
                input[hand]["type"] = "op"
    if "type" not in input[hand]:
        input[hand]["type"] = "hc"
    sortedHands[input[hand]["type"]].append(hand)

for type in sortedHands:
    sortedHands[type] = sorted(sortedHands[type], key=lambda x: [chars.index(c) for c in x])
for type in sortedHands:
    for hand in sortedHands[type]:
        winningHands.append(hand)

winnings = 0
for index, hand in enumerate(winningHands):
    multiplier = len(winningHands) - index
    #print(multiplier)
    winnings += multiplier * int(input[hand]["bid"])

print(winnings)

