import numpy as np
import pandas as pd

source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/4/" + source + ".txt"

input = np.loadtxt(file, delimiter=",", max_rows=1).astype(int)
boards = np.loadtxt(file, skiprows=1).reshape((-1,5,5)).astype(int)

winboards = []
winnumber = ()
prev = []
losboard = []
stop = False

for i in input:
  for j, b in enumerate(boards):
    b[b == i] = -i
    filtered = (b < 0)
    if filtered.all(axis = 0).any() or filtered.all(axis = 1).any():
      winboards.append(b)
      if winboards == prev:
          losboard = b
          winnumber = i
          stop = True
      else: 
        prev = winboards
    if stop:
      break
  if stop:
    break

print(losboard)
print(winnumber)

result = winnumber * np.sum(losboard[losboard > 0])

print(result)
print(winboards)