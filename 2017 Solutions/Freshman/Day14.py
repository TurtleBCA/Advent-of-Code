# # Part 1
#
# input = "hwlqcszp" + "-"
# disk = [[0 for i in range(128)] for i in range(128)]
#
# def knotHashFunction(input):
#     nums = [i for i in range(256)]
#     skipSize = 0
#     lengths = []
#     extraLengths = [17, 31, 73, 47, 23]
#     current = 0
#     for char in input:
#         lengths.append(ord(char))
#     for i in extraLengths:
#         lengths.append(i)
#
#     for r in range(64):
#         for i in lengths:
#             tmp = []
#             start = current
#             for j in range(i):
#                 tmp.append(nums[current])
#                 current = (current + 1) % 256
#             tmp.reverse()
#             for j in range(i):
#                 nums[(start + j) % 256] = tmp[j]
#             current = (current + skipSize) % 256
#             skipSize += 1
#
#     startFrom = 0
#     finalList = []
#     finalElement = ""
#     for i in range(16):
#         tmp = nums[startFrom:startFrom + 16]
#         cumulative = tmp[0] ^ tmp[1]
#         for j in tmp[2:]:
#             cumulative ^= j
#         startFrom += 16
#
#         finalElement = str(hex(cumulative)[2:])
#         if len(finalElement) == 2:
#             finalList.append(finalElement)
#         else:
#             finalList.append("0" + finalElement)
#
#     final = ""
#     for i in finalList:
#         final += i
#     return final
#
# for i in range(128):
#     binary = str(bin(int(knotHashFunction(input + str(i)), 16))[2:].zfill(128))
#     for j in range(len(disk[i])):
#         disk[i][j] = int(binary[j])
#
# useCount = 0
# for i in disk:
#     for j in i:
#         if j == 1:
#             useCount += 1
#
# print(useCount)
# for i in disk:
#     print(i)

# Part 2

file = open("Day14PossibleDisk.txt", "r")
disk = []
for line in file:
    line = line.strip()[1:-1]
    lineList = line.split(", ")
    for i in range(len(lineList)):
        lineList[i] = int(lineList[i])
    disk.append(lineList)

def key(row, column):
    return str(row) + ":" + str(column)

used = []

relationsDict = {}
for i in range(128):
    for j in range(128):
        relationsDict[key(i, j)] = []

        if disk[i][j] == 1:
            used.append(key(i, j))
            if i >= 1:
                if disk[i - 1][j] == 1:
                    relationsDict[key(i, j)].append(key(i - 1, j))
            if j <= 126:
                if disk[i][j + 1] == 1:
                    relationsDict[key(i, j)].append(key(i, j + 1))
            if i <= 126:
                if disk[i + 1][j] == 1:
                    relationsDict[key(i, j)].append(key(i + 1, j))
            if j >= 1:
                if disk[i][j - 1] == 1:
                    relationsDict[key(i, j)].append(key(i, j - 1))

groupCount = 0
already = []

def countGroups(bit):
    if bit not in already:
        already.append(bit)
        for i in relationsDict[bit]:
            countGroups(i)

for i in used:
    if i not in already:
        countGroups(i)
        groupCount += 1

print(groupCount)