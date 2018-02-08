keys2 = []
keys3 = []
values2 = []
values3 = []

file = open("Day21Input.txt", "r")
counter = 0
for line in file:
    nextLine = line.strip().split(" => ")

    currentLine = []
    nextKey = []
    for char in nextLine[0]:
        if char == "/":
            nextKey.append(currentLine)
            currentLine = []
            continue
        else:
            currentLine.append(char)
    nextKey.append(currentLine)

    currentLine = []
    nextValue = []
    for char in nextLine[1]:
        if char == "/":
            nextValue.append(currentLine)
            currentLine = []
            continue
        else:
            currentLine.append(char)
    nextValue.append(currentLine)

    if counter < 6:
        keys2.append(nextKey)
        values2.append(nextValue)
    else:
        keys3.append(nextKey)
        values3.append(nextValue)

    counter += 1

def rotate(grid, divisor):
    if divisor == 2:
        newGrid = [[" " for i in range(2)] for j in range(2)]
        newGrid[0][0] = grid[1][0]
        newGrid[0][1] = grid[0][0]
        newGrid[1][1] = grid[0][1]
        newGrid[1][0] = grid[1][1]
    elif divisor == 3:
        newGrid = [[" " for i in range(3)] for j in range(3)]
        newGrid[1][1] = grid[1][1]
        newGrid[0][0] = grid[2][0]
        newGrid[0][1] = grid[1][0]
        newGrid[0][2] = grid[0][0]
        newGrid[1][2] = grid[0][1]
        newGrid[2][2] = grid[0][2]
        newGrid[2][1] = grid[1][2]
        newGrid[2][0] = grid[2][2]
        newGrid[1][0] = grid[2][1]
    return newGrid

def flip(grid, divisor):
    if divisor == 2:
        newGrid = [[" " for i in range(2)] for j in range(2)]
        newGrid[0][0] = grid[0][1]
        newGrid[0][1] = grid[0][0]
        newGrid[1][0] = grid[1][1]
        newGrid[1][1] = grid[1][0]
    elif divisor == 3:
        newGrid = [[" " for i in range(3)] for j in range(3)]
        newGrid[0][1] = grid[0][1]
        newGrid[1][1] = grid[1][1]
        newGrid[2][1] = grid[2][1]
        newGrid[0][0] = grid[0][2]
        newGrid[0][2] = grid[0][0]
        newGrid[1][0] = grid[1][2]
        newGrid[1][2] = grid[1][0]
        newGrid[2][0] = grid[2][2]
        newGrid[2][2] = grid[2][0]
    return newGrid

def determineNew(grid, divisor):
    for i in range(2):
        for j in range(4):
            if divisor == 2:
                if grid in keys2:
                    return values2[keys2.index(grid)]
            elif divisor == 3:
                if grid in keys3:
                    return values3[keys3.index(grid)]
            grid = rotate(grid, divisor)
        grid = flip(grid, divisor)


pattern = [[".", "#", "."],
           [".", ".", "#"],
           ["#", "#", "#"]]

# pattern = [[i for i in range(9)] for j in range(9)]

# pattern = [[".", "."],
#            [".", "."]]

# tmp = determineNew(pattern, 3)
# for i in tmp:
#     print(i)

for i in pattern:
    print(i)
print("--------------")

for i in range(4):
    newPattern = []
    subPattern = []
    starts = []
    subGridList = []
    finalGrid = []
    maxK = 0
    if len(pattern) % 2 == 0:
        # Determine starts
        accumulativeJ = 0
        for j in range(0, len(pattern), 2):
            accumulativeK = 0
            for k in range(0, len(pattern[j]), 2):
                newK = k + accumulativeK
                starts.append([j + accumulativeJ, newK])
                if newK > maxK:
                    maxK = newK
                accumulativeK += 1
            accumulativeJ += 1
        # Determine subgrid and add
        for j in range(0, len(pattern), 2):
            for k in range(0, len(pattern[j]), 2):
                subGrid = [[pattern[j][k], pattern[j][k + 1]],
                           [pattern[j + 1][k], pattern[j + 1][k + 1]]]
                subGridList.append(determineNew(subGrid, 2))

        finalGrid = [[j for j in range(maxK + 3)] for k in range(maxK + 3)]
        for j in range(len(subGridList)):
            for k in range(len(subGridList[j])):
                for l in range(len(subGridList[j][k])):
                    finalGrid[starts[j][0] + k][starts[j][1] + l] = subGridList[j][k][l]

    elif len(pattern) % 3 == 0:
        accumulativeJ = 0
        for j in range(0, len(pattern), 3):
            accumulativeK = 0
            for k in range(0, len(pattern[j]), 3):
                newK = k + accumulativeK
                starts.append([j + accumulativeJ, newK])
                if newK > maxK:
                    maxK = newK
                accumulativeK += 1
            accumulativeJ += 1

        for j in range(0, len(pattern), 3):
            for k in range(0, len(pattern[j]), 3):
                subGrid = [[pattern[j][k], pattern[j][k + 1], pattern[j][k + 2]],
                           [pattern[j + 1][k], pattern[j + 1][k + 1], pattern[j + 1][k + 2]],
                           [pattern[j + 2][k], pattern[j + 2][k + 1], pattern[j + 2][k + 2]]]
                subGridList.append(determineNew(subGrid, 3))

        finalGrid = [[j for j in range(maxK + 4)] for k in range(maxK + 4)]
        for j in range(len(subGridList)):
            for k in range(len(subGridList[j])):
                for l in range(len(subGridList[j][k])):
                    finalGrid[starts[j][0] + k][starts[j][1] + l] = subGridList[j][k][l]
    for j in finalGrid:
        print(j)
    print("--------------")
    pattern = finalGrid

onCounter = 0
for i in range(len(pattern)):
    for j in range(len(pattern[i])):
        if pattern[i][j] == "#":
            onCounter += 1
print(onCounter)