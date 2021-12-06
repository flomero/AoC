import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/6/" + source + ".txt"
input = np.loadtxt(file, delimiter=",", dtype="u8")
run = "test"

if run == "test":
    days = 18
elif run == "data":
    days = 80
else:
    days = 256


for d in range(days):
    new = np.count_nonzero(input == 0)
    input[input == 0] = 9
    input[(input > 0) & (input < 9)] = input[(input > 0) & (input < 9)] - 1
    input[input == 9] = 6
    input = np.append(input, [8] * new)
    input = input.astype("u8")
    print(d)
    print(input)

print(input.shape)


