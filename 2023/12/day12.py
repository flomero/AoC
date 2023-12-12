import pprint


day = "12"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

input = []
result = 0

with open(file, "r") as f:
    for line in f:
        input.append(line.strip())

possible = {
}

def check(conditions, counts, index):
    for cpos, c in enumerate(conditions):
        if c == "?":
            conditions = conditions[:cpos] + "#" + conditions[cpos+1:]
            check(conditions, counts, index)
            conditions = conditions[:cpos] + "." + conditions[cpos+1:]
            check(conditions, counts, index)
            return
    matches = conditions.split(".")
    matches = [match for match in matches if match != ""]
    #print(matches)
    if len(matches) != len(counts):
        return
    for m, match in enumerate(matches):  
        if len(match) != counts[m]:
            return
    possible[index] = possible.get(index, 0) + 1
    #print("true")

for index, line in enumerate(input):
    counts = line.split(" ")[1].split(",")
    counts = [int(i) for i in counts]
    conditions = line.split(" ")[0]
    print(index, conditions)
    check(conditions, counts, index)
    print(possible.get(index, 0))

pprint.pprint(possible)
print(sum(possible.values()))
