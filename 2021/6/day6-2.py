import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/6/" + source + ".txt"
input = np.loadtxt(file, delimiter=",", dtype="u8")

c = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for key in c:
    n = np.count_nonzero(input == key)
    c[key] = n

for d in range(256):
    x = {0:c[1],1:c[2],2:c[3],3:c[4],4:c[5],5:c[6],6:(c[7] + c[0]),7:c[8],8:c[0]}
    c = x

result = 0
for key in c:
    result = result + c[key]
print(result)