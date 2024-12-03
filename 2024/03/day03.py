day = "03"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2024/" + day + "/" + source + ".txt"

import re

pattern = r"mul\(\d+,\d+\)"
result = 0

with open(file, 'r') as f:
	for line in f:
		matches = re.findall(pattern, line)
		for match in matches:
			result +=  int(match.split("(")[1].split(",")[0]) * int(match.split(",")[1].split(")")[0])

print(result)

pattern= r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

do = True
result = 0

with open(file, 'r') as f:
	for line in f:
		matches = re.findall(pattern, line)
		for match in matches:
			if match == "do()":
				do = True
			elif match == "don't()":
				do = False
			else:
				if do:
					result +=  int(match.split("(")[1].split(",")[0]) * int(match.split(",")[1].split(")")[0])

print(result)