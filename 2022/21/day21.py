day = "21"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

numberapes = {}
mathapes = {}
def parseApe(line: str):
    ape = line.strip().split(": ")
    if ape[1].isnumeric():
        numberapes[ape[0]] = int(ape[1])
    else:
        first, op, second = ape[1].split(" ")
        mathapes[ape[0]] = {
            "first": first,
            "second": second,
            "op": op
        }


with open(file, "r") as f:
    for line in f:
        parseApe(line)

while len(mathapes) > 0:
    for name in list(mathapes):
        ape = mathapes[name]
        print(ape)
        if ape["first"] in numberapes and ape["second"] in numberapes:
            new = 0
            if ape["op"] == "+":
                new = numberapes[ape["first"]] + numberapes[ape["second"]]
            elif ape["op"] == "-":
                new = numberapes[ape["first"]] - numberapes[ape["second"]]
            elif ape["op"] == "/":
                new = numberapes[ape["first"]] / numberapes[ape["second"]]
            elif ape["op"] == "*":
                new = numberapes[ape["first"]] * numberapes[ape["second"]]
            numberapes[name] = new
            del mathapes[name]

print(numberapes)
print(numberapes["root"])