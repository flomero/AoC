import numpy as np

day = "09"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

dt = np.dtype([('dir', np.unicode_, 1),("steps", np.int_)])
input = np.genfromtxt(file, delimiter=" ", dtype=dt)

head = np.array([0, 0])
tail = np.array([0, 0])

visitedTail = np.array([[0, 0]])

def checkTouching(a, b):
    x_diff = abs(a[0] - b[0])
    y_diff = abs(a[1] - b[1])
    if x_diff == 1 and y_diff == 0:
        return True
    elif x_diff == 0 and y_diff == 1:
        return True
    elif x_diff == 1 and y_diff == 1:
        return True
    elif x_diff == 0 and y_diff == 0:
        return True
    else:
        return False

def checkStraight(a, b):
    x_diff = abs(a[0] - b[0])
    y_diff = abs(a[1] - b[1])
    if y_diff == 0 and x_diff != 0 :
        return True
    elif x_diff == 0 and y_diff != 0:
        return True
    else:
        return False

def move_point_towards(a, b):
  x_diff = a[0] - b[0]
  y_diff = a[1] - b[1]
  if x_diff > 0 and y_diff > 0:
    return [1, 1]
  elif x_diff > 0 and y_diff < 0:
    return [1, -1]
  elif x_diff < 0 and y_diff > 0:
    return [-1, 1]
  elif x_diff < 0 and y_diff < 0:
    return [-1, -1]
  else:
    return [0, 0]

for line in input:
    dir = line[0]
    steps = line[1]
    for i in range(steps):
        if dir == "R":
            head = head + np.array([0,1])
            if checkTouching(head, tail):
                tail = tail
            elif checkStraight(head, tail):
                tail = tail + np.array([0,1])
            else:
                tail = tail + np.array(move_point_towards(head, tail))
        elif dir == "L":
            head = head + np.array([0,-1])
            if checkTouching(head, tail):
                tail = tail
            elif checkStraight(head, tail):
                tail = tail + np.array([0,-1])
            else:
                tail = tail + np.array(move_point_towards(head, tail))
        elif dir == "U":
            head = head + np.array([1,0])
            if checkTouching(head, tail):
                tail = tail
            elif checkStraight(head, tail):
                tail = tail + np.array([1,0])
            else:
                tail = tail + np.array(move_point_towards(head, tail))
        elif dir == "D":
            head = head + np.array([-1,0])
            if checkTouching(head, tail):
                tail = tail
            elif checkStraight(head, tail):
                tail = tail + np.array([-1,0])
            else:
                tail = tail + np.array(move_point_towards(head, tail))
        visitedTail = np.vstack([visitedTail, tail])

print(head)
print(tail)
partOne = (len(np.unique(visitedTail, axis=0)))

print(partOne)

visitedTail = np.array([[0, 0]])
start = np.array([0, 0])
knots = np.array([start for _ in range(10)])

for line in input:
    dir = line[0]
    steps = line[1]
    for _ in range(steps):
        visitedTail = np.vstack([visitedTail, knots[-1]])
        if dir == "D":
            knots[0] += [-1, 0]
        elif dir == "U":
            knots[0] += [1, 0]
        elif dir == "R":
            knots[0] += [0, 1]
        elif dir == "L":
            knots[0] += [0, -1]
        for i, ((ay, ax), (by, bx)) in enumerate(zip(knots, knots[1:])):
            if abs(ay-by) > 1:
                by += 1 if ay > by else -1
                if abs(ax - bx) > 0:
                    bx += 1 if ax > bx else -1
            elif abs(ax - bx) > 1:
                bx += 1 if ax > bx else -1
                if abs(ay - by) > 0:
                    by += 1 if ay > by else -1
            knots[i + 1][0] = by
            knots[i + 1][1] = bx
 

partTwo = (len(np.unique(visitedTail, axis=0)) + 1)
print(partTwo)

