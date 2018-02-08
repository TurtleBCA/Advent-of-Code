# Part 2

# pos = []
# vel = []
# acc = []
#
# file = open("Day20Input.txt", "r")
# for line in file:
#     three = line.split(", ")
#     for i in range(len(three)):
#         three[i] = three[i].strip()[3:-1]
#         finalList = three[i].split(",")
#         for j in range(len(finalList)):
#             finalList[j] = int(finalList[j])
#         if i == 0:
#             pos.append(finalList)
#         elif i == 1:
#             vel.append(finalList)
#         else:
#             acc.append(finalList)
#
# def distance(pos):
#     return abs(pos[0]) + abs(pos[1]) + abs(pos[2])
#
# closestPoints = []
#
# for i in range(1000):
#     closestDist = distance(pos[0])
#     closestId = 0
#     for j in range(len(pos)):
#         for k in range(len(acc[j])):
#             vel[j][k] += acc[j][k]
#             pos[j][k] += vel[j][k]
#         localDist = distance(pos[j])
#         if localDist < closestDist:
#             closestDist = localDist
#             closestId = j
#     print(closestId)
# Take last printed id

# Part 2

pos = []
vel = []
acc = []

file = open("Day20Input.txt", "r")
for line in file:
    three = line.split(", ")
    for i in range(len(three)):
        three[i] = three[i].strip()[3:-1]
        finalList = three[i].split(",")
        for j in range(len(finalList)):
            finalList[j] = int(finalList[j])
        if i == 0:
            pos.append(finalList)
        elif i == 1:
            vel.append(finalList)
        else:
            acc.append(finalList)

lowest = 1000
for i in range(1000):
    if len(pos) < lowest:
        lowest = len(pos)
        print(lowest)
    seen = []
    toDestroy = []
    for j in range(len(pos)):
        for k in range(len(acc[j])):
            vel[j][k] += acc[j][k]
            pos[j][k] += vel[j][k]
        if pos[j] not in seen:
            seen.append(pos[j])
        else:
            toDestroy.append(pos[j])
    for j in toDestroy:
        for k in range(len(pos)):
            try:
                del vel[pos.index(j)]
                del acc[pos.index(j)]
                pos.remove(j)
            except ValueError:
                break

# Not 961 (Too high)