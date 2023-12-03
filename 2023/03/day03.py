import re
import numpy as np

day = "03"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

input = np.genfromtxt(file, dtype=str, delimiter="", comments=None)

print(input)

result = 0

numbers = {}
gears = {}

def specialChar(char):
    return re.match(r'[^0-9\.]', char)
    
def addGear(i, j, number):
    pos = str(i) + "-" + str(j)
    gears[pos] = gears.get(pos, list())
    gears[pos].append(number)
    

for i in range(input.shape[0]):
    newNumber = True
    number = ""
    for j in range(len(input[i])):
        if re.match(r'\d', input[i][j]):
            if newNumber:
                number = input[i][j]
                newNumber = False
            else:
                number += input[i][j]
        if re.match(r'\D', input[i][j]) or j == len(input[i])-1:
            eol = bool(j == len(input[i])-1 and re.match(r'\d', input[i][j]))
            newNumber = True
            if number: 
                s = len(number)
                if input[i][j] == "*":
                    addGear(i, j, number)
                if specialChar(input[i][j]):
                    print(number)
                    result += int(number)
                    number = ""
                    continue
                if eol:
                    s = s-1
                if input[i][j-s-1] == "*":
                    addGear(i, j-s-1, number)
                if specialChar(input[i][j-s-1]):
                    print(number)
                    result += int(number)
                    number = ""
                    continue
                for k in [-1, 1]:
                    for l in range(s+2):
                        if (i+k) < 0 or (i+k) >= input.shape[0]:
                            continue
                        if (j-s-1+l) < 0 or (j-s-1+l) >= len(input[i+k]):
                            continue
                        if input[i+k][j-s-1+l] == "*":
                            addGear(i+k, j-s-1+l, number)
                        if specialChar(input[i+k][j-s-1+l]):
                            print(number)
                            result += int(number)
                            number = ""
                            continue
            number = ""

print(result)
result2 = 0
                
for g in gears:
    if len(gears[g]) == 2:        
        ratio = int(gears[g][0])*int(gears[g][1])
        result2 += ratio

print(result2)



