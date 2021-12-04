from typing import Counter
import numpy as np
import pandas as pd

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/4/" + source + ".txt"

input = np.loadtxt(file, delimiter=",", max_rows=1).astype(int)
boards = np.loadtxt(file, skiprows=1).reshape((-1,5,5)).astype(int)

number = ()
losboard = []
values = [False] * len(boards)
stop = False

for i in input:
  for j, b in enumerate(boards):
    if values[j] == False:
        if i != 0:
            b[b == i] = -i
        else:
            b[b == i] = -1
        filtered = (b < 0)
        if filtered.all(axis = 0).any() or filtered.all(axis = 1).any():
            values[j] = True
        if values.count(False) == 0:
            losboard = b
            number = i
            stop = True
            break
    if stop:
      break
  if stop:
    break

print(losboard)
print(number)
sum = np.sum(losboard[losboard > 0])
print(sum)
result = number * sum
print(result)