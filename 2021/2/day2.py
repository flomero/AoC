source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/2/" + source + ".txt"

with open(file, 'r') as f:
  list = f.read().splitlines()

counterHor = 0
counterDep = 0

for i in range(len(list)):
    input = list[i].split(" ")
    if input[0] == "down":
        counterDep = counterDep + int(input[1])
    elif  input[0] == "up":
        counterDep = counterDep - int(input[1])
    elif input[0] == "forward":
        counterHor = counterHor + int(input[1])

print("horizontal: " + str(counterHor))
print("Tiefe: " + str(counterDep))
product = counterHor * counterDep
print("Produkt: " + str(product))

counterHor = 0
counterDep = 0
counterAim = 0

for i in range(len(list)):
    input = list[i].split(" ")
    if input[0] == "down":
        counterAim = counterAim + int(input[1])
    elif  input[0] == "up":
        counterAim = counterAim - int(input[1])
    elif input[0] == "forward":
        counterHor = counterHor + int(input[1])
        counterDep = counterDep + (counterAim * int(input[1]))

print("Aim horizontal: " + str(counterHor))
print("Aim Tiefe: " + str(counterDep))
product = counterHor * counterDep
print("Aim Produkt: " + str(product))
