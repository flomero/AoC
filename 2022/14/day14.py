import cmath
day = "14"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

with open(file, 'r') as f:
  input = f.read().splitlines()
  
walls = set()

for line in input:
    line = line.split(" -> ")
    points = []
    for point in line:
        point = point.split(",")
        p = complex(int(point[0]), int(point[1]))
        points.append(p)
    for x in range(len(points)):
        if points[x].real == points[x-1].real:
            ims = [points[x].imag, points[x-1].imag]
            ims.sort()
            for i in range(int(ims[0]), int(ims[1])):
                walls.add(complex(points[x].real, i))
        else:
            reals = [points[x].real, points[x-1].real]
            reals.sort()
            for i in range(int(reals[0]), int(reals[1])):
                walls.add(complex(i, points[x].imag))

start = complex(500, 0)

floor = (max(p.imag for p in walls))
xmin =  (min(p.real for p in walls))
xmax =  (max(p.real for p in walls))


all = set()
all.update(walls)

print(xmax, xmin)


def generateSand():
    sand = 0
    current = start
    while sand  < 10000:
        while True:
            down = current + complex(0, 1)
            left = current + complex(-1, 1)
            right = current + complex(1, 1)
            if current.imag > floor:
                print("hello")
                all.add(start)
                return
            if down not in all:
                current = down
            elif left not in all:
                current = left
            elif right not in all:
                current = right
            else:
                all.add(current)
                sand += 1   
                print(sand)
            

generateSand()
sand = all.difference(walls)

print(sand)
print(len(all) - len(walls))