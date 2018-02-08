file = open("Day11Input.txt", "r")
current = [0, 0]

for line in file:
    directions = line.strip().split(",")

for i in directions:
    if i == "nw":
        current[0] -= 1
        current[1] += 1
    elif i == "n":
        current[1] += 1
    elif i == "ne":
        current[0] += 1
    elif i == "se":
        current[0] += 1
        current[1] -= 1
    elif i == "s":
        current[1] -= 1
    elif i == "sw":
        current[0] -= 1

print(current)
distance = 0
distance = abs(current[0]) + abs(current[1])
print(distance)

# Part 2

file = open("Day11Input.txt", "r")
current = [0, 0]
distance = 0
farthest = 0

for line in file:
    directions = line.strip().split(",")

for i in directions:
    if i == "nw":
        current[0] -= 1
        current[1] += 1
    elif i == "n":
        current[1] += 1
    elif i == "ne":
        current[0] += 1
    elif i == "se":
        current[0] += 1
        current[1] -= 1
    elif i == "s":
        current[1] -= 1
    elif i == "sw":
        current[0] -= 1
    distance = abs(current[0]) + abs(current[1])
    if distance > farthest:
        farthest = distance

print(current)
print(farthest)