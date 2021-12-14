import numpy as np
import itertools
import pprint
from collections import defaultdict

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/14/" + source + ".txt"

steps = 40
rules = {}
with open(file) as f:
    template = f.readline().strip()
    for line in itertools.islice(f, 1, None):
        (key, val) = line.strip().split(" -> ")
        rules[key] = val

pairs = defaultdict(int)
chars = defaultdict(int)

for r in rules:
    pairs[r] = 0

for i, j in zip(template, template[1:]):
    pair = i + j
    pairs[pair] += 1

for c in template:
    chars[c] += 1

for s in range(steps):
    newpairs = defaultdict(int)
    for p, count in pairs.items():
        inserted = rules[p]
        if inserted is not None:
            newpairs[p[0] + inserted] += count
            newpairs[inserted + p[1]] += count
            chars[inserted] += count
        else:
            newpairs[p] += count
    pairs = newpairs

pprint.pprint(chars)
vals = chars.values()

print(max(vals) - min(vals))