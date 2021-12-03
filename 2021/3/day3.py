source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/3/" + source + ".txt"

with open(file, 'r') as f:
  list = f.read().splitlines()

gamma = ""

for p in range(len(list[1])):
    one = 0
    null = 0
    for i in range(len(list)):
        m = [*map(int,str(list[i]))]
        if m[p] == 1:
            one = one + 1
        elif m[p] == 0:
            null = null + 1
    if one > null:
        gamma = gamma + "1"
    else:
        gamma = gamma + "0"


epsilon = gamma.replace('1','2').replace('0','1').replace('2','0')

gammaInt = int(gamma, 2)
epsilonInt = int(epsilon, 2)

result = gammaInt * epsilonInt

print("Gamma: " + gamma + " - " + str(gammaInt))
print("Epsilon: " + epsilon + " - " + str(epsilonInt))
print("Result: " + str(result))