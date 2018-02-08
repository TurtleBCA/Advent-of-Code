available = []
zeroes = []

file = open("Day24Input.txt", "r")
for line in file:
    lineList = line.strip().split("/")
    lineList[0] = int(lineList[0])
    lineList[1] = int(lineList[1])
    available.append(lineList)
    if lineList[0] == 0:
        zeroes.append(lineList)

avaCopy = []
bridge = []
longest = 0

# def buildBridges(local, bridge, pPort):
#     global longest
#     localCopy = local[:]
#     localBridge = bridge[:]
#     end = True
#     already = []
#     for component in localCopy:
#         if pPort in component and (component not in already):
#             if component[0] != component[1]:
#                 for cPortInd in range(2):
#                     if component[cPortInd] == pPort:
#                         end = False
#                         localBridge.append(component)
#                         localCopy.remove(component)
#                         buildBridges(localCopy, localBridge, component[(cPortInd + 1) % 2])
#             else:
#                 if component[0] == pPort:
#                     end = False
#                     localBridge.append(component)
#                     localCopy.remove(component)
#                     buildBridges(localCopy, localBridge, component[0])
#             localBridge.remove(component)
#             localCopy.append(component)
#             already.append(component)
#     sum = 0
#     if end == True:
#         for component in localBridge:
#             for port in component:
#                 sum += port
#
#     if sum > longest:
#         print(localBridge)
#         longest = sum



def buildBridges(sum, available, bridge, port):
    print(bridge)
    global longest
    for i in available:
        if port in i:
            available.remove(i)
            bridge.append(i)
            for j in range(2):
                sum += i[j]
            if i[0] == i[1]:
                buildBridges(sum, available, bridge, i[0])
            else:
                for j in range(2):
                    if i[j] == port:
                        buildBridges(sum, available, bridge, i[(j + 1) % 2])
            for j in range(2):
                sum -= i[j]
            bridge.remove(i)

    print("End: " + str(bridge))
    test = 0
    for i in bridge:
        for j in i:
            test += j
    print("Sum says: " + str(sum) + " Test says: " + str(test))

    if test > longest:
        longest = test


for i in zeroes:
    bridge = []
    avaCopy = available[:]
    avaCopy.remove(i)
    bridge.append(i)
    # buildBridges(avaCopy, bridge, i[1])
    buildBridges(i[1], avaCopy, bridge, i[1])

print(longest)

# Not 2440 Too high
# Not 1994 Too low
# Not 2072 Too high