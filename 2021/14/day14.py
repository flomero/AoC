import numpy as np
import itertools
from collections import defaultdict

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/14/" + source + ".txt"

steps = 10
rules = {}
with open(file) as f:
    template = f.readline().strip()
    for line in itertools.islice(f, 1, None):
        (key, val) = line.strip().split(" -> ")
        rules[key] = val

for s in range(steps):
    new = ""
    for i, j in zip(template, template[1:]):
        pair = i + j
        new = new + i + rules[pair]
    template = new + template[-1]

chars = defaultdict(int)
for char in template:
    chars[char] += 1

vals = chars.values()

print(max(vals) - min(vals))