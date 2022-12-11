import math
import pprint
import re

day = "11"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

monkeys = {}

def processLines(lines):
    monkeyNumber = re.sub(r'[^0-9]', '', lines[0])
    startingItems = re.sub(r'[^0-9\,]', '', lines[1]).strip().split(",")
    operation = lines[2].split(":")[1].strip().split(" ")
    test = re.sub(r'[^0-9]', '', lines[3])
    testTrue = re.sub(r'[^0-9]', '', lines[4])
    testFalse = re.sub(r'[^0-9]', '', lines[5])
    monkeys[monkeyNumber] = {
        "startingItems": startingItems,
        "operation": operation,
        "test": int(test),
        "testTrue": testTrue,
        "testFalse": testFalse,
        "inspected": 0
    }

with open(file, 'r') as f:
    lines = []
    for line in f:
        lines.append(line)
        if len(lines) >= 7:
            processLines(lines)
            lines = []
    if len(lines) > 0:
        processLines(lines)

rounds = 10000

def operation(op, old):
    a = 0
    b = 0
    if op[2] == "old": a = old
    else: a = int(op[2])
    if op[4] == "old": b = old
    else: b = int(op[4])
    if op[3] == "+": return (a+b)
    elif op[3] == "*": return (a*b)
    else: return 0

divs = []
for m in monkeys:
    divs.append(monkeys[m]["test"])   
lcm = math.lcm(*[d for d in divs]) 

pp = pprint.PrettyPrinter(depth=6)

for i in range(rounds):
    print(i)
    for m in monkeys:
        for item in monkeys[m]["startingItems"]:
            monkeys[m]["startingItems"] = monkeys[m]["startingItems"][1:]
            ## part 1
            ## item = math.floor(int(operation(monkeys[m]["operation"], int(item))) / 3)
            ## part 2
            item = int(operation(monkeys[m]["operation"], int(item)))
            item = item % lcm
            monkeys[m]["inspected"] += 1
            if item % monkeys[m]["test"] == 0:
                target = monkeys[m]["testTrue"]
                monkeys[target]["startingItems"].append(item)
            else:
                target = monkeys[m]["testFalse"]
                monkeys[target]["startingItems"].append(item)

inspectedValues = []
for m in monkeys:
    inspectedValues.append(monkeys[m]["inspected"])

business = sorted(inspectedValues)[-1] * sorted(inspectedValues)[-2]
print(business)

