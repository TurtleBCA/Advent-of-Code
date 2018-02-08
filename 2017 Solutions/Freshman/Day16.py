# letters = "abcdefghijklmnop"
# programs = []
# for i in range(16):
#     programs.append(letters[i])
#
# dance = []
# file = open("Day16INput.txt", "r")
# for line in file:
#     lineList = line.split(",")
#     dance = lineList
#
# def spin(string):
#     global programs
#     spins = int(string)
#     programs = programs[-spins:] + programs[:-spins]
#
# def exchange(string):
#     nums = string.split("/")
#     pos1 = int(nums[0])
#     pos2 = int(nums[1])
#     tmp = programs[pos1]
#     programs[pos1] = programs[pos2]
#     programs[pos2] = tmp
#
# def partner(string):
#     nums = string.split("/")
#     pos1 = programs.index(nums[0])
#     pos2 = programs.index(nums[1])
#     tmp = programs[pos1]
#     programs[pos1] = programs[pos2]
#     programs[pos2] = tmp
#
# for i in range(len(dance)):
#     kind = dance[i][0]
#     dance[i] = dance[i][1:]
#     if kind == "s":
#         spin(dance[i])
#     elif kind == "x":
#         exchange(dance[i])
#     elif kind == "p":
#         partner(dance[i])
#
# final = ""
# for i in programs:
#     final += i
#
# print(final)

# Part 2

letters = "dcmlhejnifpokgba"
programs = []
for i in range(16):
    programs.append(letters[i])

dance = []
file = open("Day16Input.txt", "r")
for line in file:
    lineList = line.split(",")
    dance = lineList

def spin(string):
    global programs
    spins = int(string)
    programs = programs[-spins:] + programs[:-spins]

def exchange(string):
    nums = string.split("/")
    pos1 = int(nums[0])
    pos2 = int(nums[1])
    tmp = programs[pos1]
    programs[pos1] = programs[pos2]
    programs[pos2] = tmp

def partner(string):
    nums = string.split("/")
    pos1 = programs.index(nums[0])
    pos2 = programs.index(nums[1])
    tmp = programs[pos1]
    programs[pos1] = programs[pos2]
    programs[pos2] = tmp

already = []
alphabet = "abcdefghijklmnop"
already.append([i for i in alphabet])
alreadyIter = [0]
iteration = 10000
dances = 1
print(1000000000 % 24)
while dances < 16:
    for i in range(len(dance)):
        iteration += 1
        kind = dance[i][0]
        now = dance[i][1:]

        if kind == "s":
            spin(now)
        elif kind == "x":
            exchange(now)
        elif kind == "p":
            partner(now)
    dances += 1

    if programs not in already:
        already.append(programs[:])
        alreadyIter.append(iteration)
    else:
        print("Currently at", iteration)
        print("Already done at", alreadyIter[already.index(programs[:])])
        print(programs)
        print(already[already.index(programs[:])])
    if dances == 16 or dances == 2:
        print(programs)
    print(dances)

final = ""
for i in programs:
    final += i

print(final)

# not nmafleciobjgdkph

# Every 24 dances, abcdefghijklmnop returns.
# 1000000000 % 24 == 16
# Answer: ifocbejpdnklamhg