# Part 1

input = 325489
biggestSquare = 1
brCoordinate = [0,0]
while input > biggestSquare ** 2:
    biggestSquare += 2
    brCoordinate[0] += 1
    brCoordinate[1] -= 1
    print(biggestSquare ** 2)
    print(brCoordinate)

print(biggestSquare)

blCoordinate = [-brCoordinate[0], brCoordinate[1]]
tlCoordinate = [-brCoordinate[0], -brCoordinate[1]]
trCoordinate = [brCoordinate[0], -brCoordinate[1]]

blValue = (biggestSquare ** 2) - (biggestSquare - 1)
print(blValue)

difference = (biggestSquare ** 2) - input
print(difference)
inputPoint = [brCoordinate[0] - difference, blCoordinate[1]]
distance = abs(inputPoint[0]) + abs(inputPoint[1])
print(distance)

# Part 2

matrix = [[0 for x in range(51)] for y in range(51)]
matrix[25][25] = 1
current = [26, 25]
growth = 0
while growth < 325489:
    growth = 0
    growth += matrix[current[0] + 1][current[1]]
    growth += matrix[current[0] + 1][current[1] + 1]
    growth += matrix[current[0]][current[1] + 1]
    growth += matrix[current[0] - 1][current[1] + 1]
    growth += matrix[current[0] - 1][current[1]]
    growth += matrix[current[0] - 1][current[1] - 1]
    growth += matrix[current[0]][current[1] - 1]
    growth += matrix[current[0] + 1][current[1] - 1]
    matrix[current[0]][current[1]] = growth
    if matrix[current[0]][current[1] + 1] != 0 and matrix[current[0] + 1][current[1]] == 0:
        current[0] += 1
    elif matrix[current[0] - 1][current[1]] != 0 and matrix[current[0]][current[1] + 1] == 0:
        current[1] += 1
    elif matrix[current[0]][current[1] - 1] != 0 and matrix[current[0] - 1][current[1]] == 0:
        current[0] -= 1
    elif matrix[current[0] + 1][current[1]] != 0 and matrix[current[0]][current[1] - 1] == 0:
        current[1] -= 1

    for row in matrix:
        print(row)

print(growth)
for row in matrix:
    print(row)