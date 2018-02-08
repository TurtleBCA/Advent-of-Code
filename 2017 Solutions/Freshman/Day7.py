# Part 1

file = open("Day7Input.txt", "r")
orderDict = {}
top = {}
weightDict = {}
for line in file:
    lineList = line.strip().split()
    for i in range(len(lineList)):
        lineList[i] = lineList[i].replace(",", "")
    lineList[1] = int(lineList[1][1:-1])

    if len(lineList) > 2:
        orderDict[lineList[0]] = lineList[3:]
    else:
        top[lineList[0]] = lineList[1]

    weightDict[lineList[0]] = lineList[1]

    print(lineList)

current = "dsiixv"
keys = list(orderDict.keys())
while True:
    con = False
    for i in keys:
        if current in orderDict[i]:
            current = i
            con = True
            break
    if con == True:
        continue
    else:
        break

print(current)

# Part 2

# for i in orderDict:
#     for j in orderDict[i]:
#         possible = []
#         for k in top:
#             if k in j:
#                 possible.append(k)
#         if len(possible) == 0:
#             continue
#         weight = top[possible[0]]
#         valid = True
#         for k in possible:
#             if top[k] != weight:
#                 valid = False
#                 print(i)
#                 break
#             else:
#                 sum = 0
#                 for l in possible:
#                     sum += weightDict[l]
#                 weightDict[i] = weightDict[i] + sum
#                 top[i] = weightDict[i]

print(orderDict)
print(weightDict)

totalDict = {}
def findWeight(program):
    localWeight = weightDict[program]
    if program in orderDict:
        for subProgram in orderDict[program]:
            localWeight += findWeight(subProgram)
    totalDict[program] = localWeight
    return localWeight

findWeight("cqmvs")
print(totalDict)

def checkWeight(program):
    topWeight = totalDict[program] - weightDict[program]
    if topWeight % len(orderDict[program]) != 0:
        for subProgram in orderDict[program]:
            checkWeight(subProgram)
    else:
        print(program)
        return program

print(checkWeight("cqmvs"))
print(totalDict["vmttcwe"])
print(totalDict["ukwlfcf"])
print(totalDict["zzpevgd"])
for i in orderDict["vmttcwe"]:
    print(totalDict[i])
print(weightDict["vmttcwe"] + (99 * 3))

#Answer
print("Answer: " + str(weightDict["vmttcwe"] - 8))

print(totalDict["vmttcwe"] + totalDict["ukwlfcf"] + totalDict["zzpevgd"] + weightDict["bntzksk"])
print(weightDict["bntzksk"])