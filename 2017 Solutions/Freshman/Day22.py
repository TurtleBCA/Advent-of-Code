# Part 1

# file = open("Day22Input.txt", "r")
# grid = []
# for line in file:
#     row = []
#     for i in line.strip():
#         row.append(i)
#     grid.append(row)
#
# # grid = [[".", ".", "#"], ["#", ".", "."], [".", ".", "."]]
#
# current = [len(grid[0]) // 2, len(grid[0]) // 2]
#
# direction = 0
#
# counter = 0
# for i in range(10000):
#     gridPos = grid[current[0]][current[1]]
#     if gridPos == "#":
#         direction = (direction + 1) % 4
#     else:
#         direction = (direction - 1) % 4
#
#     if gridPos == ".":
#         grid[current[0]][current[1]] = "#"
#         counter += 1
#     else:
#         grid[current[0]][current[1]] = "."
#
#     if direction == 0:
#         if current[0] == 0:
#             newGrid = [["." for i in range(len(grid[0]))]]
#             for i in grid:
#                 newGrid.append(i)
#             grid = newGrid
#             current[0] += 1
#         current[0] -= 1
#     elif direction == 1:
#         if current[1] == len(grid[0]) - 1:
#             for i in range(len(grid)):
#                 grid[i].append(".")
#         current[1] += 1
#     elif direction == 2:
#         if current[0] == len(grid) - 1:
#             grid.append(["." for i in range(len(grid[0]))])
#         current[0] += 1
#     elif direction == 3:
#         if current[1] == 0:
#             for i in range(len(grid)):
#                 grid[i].insert(0, ".")
#             current[1] += 1
#         current[1] -= 1
#
# print(counter)

# Answer 5433

# Part 2

file = open("Day22Input.txt", "r")
grid = []
for line in file:
    row = []
    for i in line.strip():
        row.append(i)
    grid.append(row)

# grid = [[".", ".", "#"], ["#", ".", "."], [".", ".", "."]]

current = [len(grid[0]) // 2, len(grid[0]) // 2]

direction = 0

counter = 0
for i in range(10000000):
    gridPos = grid[current[0]][current[1]]
    if gridPos == ".":
        direction = (direction - 1) % 4
    elif gridPos == "#":
        direction = (direction + 1) % 4
    elif gridPos == "F":
        direction = (direction + 2) % 4

    if gridPos == ".":
        grid[current[0]][current[1]] = "W"
    elif gridPos == "W":
        grid[current[0]][current[1]] = "#"
        counter += 1
    elif gridPos == "#":
        grid[current[0]][current[1]] = "F"
    else:
        grid[current[0]][current[1]] = "."

    if direction == 0:
        if current[0] == 0:
            newGrid = [["." for i in range(len(grid[0]))]]
            for i in grid:
                newGrid.append(i)
            grid = newGrid
            current[0] += 1
        current[0] -= 1
    elif direction == 1:
        if current[1] == len(grid[0]) - 1:
            for i in range(len(grid)):
                grid[i].append(".")
        current[1] += 1
    elif direction == 2:
        if current[0] == len(grid) - 1:
            grid.append(["." for i in range(len(grid[0]))])
        current[0] += 1
    elif direction == 3:
        if current[1] == 0:
            for i in range(len(grid)):
                grid[i].insert(0, ".")
            current[1] += 1
        current[1] -= 1

print(counter)