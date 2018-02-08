# Part 1

relationsDict = {}
file = open("Day12Input.txt", "r")
counter = 0
for line in file:
    relationsDict[counter] = []
    relationsCollection = []
    lineList = line.strip().split(" ")
    for conInd in range(len(lineList[2:])):
        conInd += 2
        if conInd < len(lineList) - 1:
            lineList[conInd] = lineList[conInd][:-1]
        relationsCollection.append(int(lineList[conInd]))
    relationsDict[counter] = relationsCollection
    counter += 1

already = []
conCount = 0

def countConnections(program):
    global conCount
    if program not in already:
        conCount += 1
        already.append(program)
        for i in relationsDict[program]:
            countConnections(i)

countConnections(0)
print(conCount)

# Part 2

groupCount = 0
already = []

def countGroups(program):
    if program not in already:
        already.append(program)
        for i in relationsDict[program]:
            countGroups(i)

for i in range(2000):
    if i not in already:
        countGroups(i)
        groupCount += 1

print(groupCount)
