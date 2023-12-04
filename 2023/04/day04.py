import re
import pprint

day = "04"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

cards = {}

with open(file) as f:
    for line in f:
        split = line.split(": ")
        cards[split[0].split()[1]] = {}
        numbers = split[1].split(" | ")
        winning = numbers[0].split()
        scratched = numbers[1].strip().split()
        cards[split[0].split()[1]]["w"] = winning
        cards[split[0].split()[1]]["s"] = scratched

for card in cards:
    for n in cards[card]['s']:
        if n in cards[card]['w']:
            cards[card]['matches'] = cards[card].get('matches', 0) + 1

result = 0
for card in cards:
   if cards[card].get('matches', False):
    result += 2 ** (cards[card]['matches']-1)

#pprint.pprint(cards)
print(result)

result2 = 0
for card in cards:
    if not cards[card].get('count', False):
        cards[card]['count'] = 1
    if cards[card].get('matches', False):
        matches = (cards[card]['matches'])
        for i in range(1, matches + 1):
            next = str(int(card) + i)
            if next in cards:
                cards[next]['count'] = cards[next].get('count', 1) + 1 + cards[card]['count'] - 1

for card in cards:
    result2 += cards[card]['count']
        

print(result2)
