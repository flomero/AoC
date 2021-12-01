file = "C:/Users/flofi/repos/CodeImAdvent/2021/1/" + "data.txt"

with open(file, 'r') as f:
  list = f.read().splitlines()

print(list)  

counter = 0

for i in range(len(list)):
    if i < len(list) - 1:
        if list[i] < list[i+1]:
            counter = counter + 1

print(counter)

