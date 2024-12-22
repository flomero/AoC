from pprint import pprint
import pyperclip
from collections import deque
from functools import lru_cache
import itertools
from collections import defaultdict

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "22"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().splitlines()

data = list(map(int, rawdata))

@lru_cache
def next_secret(secret):
	secret ^= (secret * 64)
	secret %= 16777216
	secret ^= (secret // 32)
	secret %= 16777216
	secret ^= (secret * 2048)
	secret %= 16777216
	return secret

def generate_nth_secret(initial, n):
	secret = initial
	for _ in range(n):
		secret = next_secret(secret)
	return secret

result = 0
for secret in data:
	  result += generate_nth_secret(secret, 2000)

printc(result)

sequences = set()
results = []
seqres = []

for secret in data:
	current = []
	for _ in range(2000):
		start = secret % 10
		secret = next_secret(secret)
		current.append((secret, (secret % 10) - start))

	seqs = {}
	for i in range(len(current) - 3):
		seq = [current[i][1], current[i+1][1], current[i+2][1], current[i+3][1]]
		seq = tuple(seq)
		if seq not in seqs:
			seqs[seq] = current[i + 3][0] % 10

	seqres.append(seqs)
	results.append(current)
	sequences.update(seqs.keys())

result = 0
for seq in sequences:
	total = 0
	for res, sres in zip(results, seqres):
		if seq not in sres:
			continue
		total += sres[seq]
	result = max(result, total)

printc(result)
