# Part 1

firewall = [[0] for i in range(99)]
direction = {}
special = []
file = open("Day13Input.txt", "r")

for line in file:
    lineList = line.strip().split(": ")
    firewall[int(lineList[0])] = [0 for i in range(int(lineList[1]))]
    firewall[int(lineList[0])][0] = 1
    direction[int(lineList[0])] = 0
    special.append(int(lineList[0]))

current = -1
caught = []
for i in range(99):
    current += 1
    if firewall[current][0] == 1:
        caught.append(current)
    for i in special:
        if firewall[i][0] == 1:
            direction[i] = 0
        elif firewall[i][len(firewall[i]) - 1] == 1:
            direction[i] = 1
        if direction[i] == 0:
            firewall[i] = [firewall[i][-1]] + firewall[i][:-1]
        elif direction[i] == 1:
            firewall[i] = firewall[i][1:] + [firewall[i][0]]

severity = 0
for i in caught:
    severity += i * len(firewall[i])

print(severity)

# Part 2

firewall = [[0] for i in range(99)]
direction = {}
special = []
file = open("Day13Input.txt", "r")
original = []

for line in file:
    lineList = line.strip().split(": ")
    firewall[int(lineList[0])] = [0 for i in range(int(lineList[1]))]
    firewall[int(lineList[0])][0] = 1
    direction[int(lineList[0])] = 0
    special.append(int(lineList[0]))
original = firewall

def iterate(matrix, direction):
    for i in special:
        if matrix[i][0] == 1:
            direction[i] = 0
        elif matrix[i][len(matrix[i]) - 1] == 1:
            direction[i] = 1
        if direction[i] == 0:
            matrix[i] = [matrix[i][-1]] + matrix[i][:-1]
        elif direction[i] == 1:
            matrix[i] = matrix[i][1:] + [matrix[i][0]]

clear = False
delay = 0
firewallCopy = []
directionCopy = {}
while not clear:
    iterate(firewall, direction)
    delay += 1

    clear = True
    current = -1

    firewallCopy = firewall[:]
    directionCopy = direction.copy()
    for i in range(99):
        current += 1
        if firewallCopy[current][0] == 1:
            clear = False
            break
        iterate(firewallCopy, directionCopy)
    print(delay)

print(delay)

# Answer: 3830344