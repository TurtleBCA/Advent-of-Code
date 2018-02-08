# Part 1

# file = open("Day18Input.txt", "r")
# reg = {}
# before = 0
# ins = []
# for line in file:
#     ins.append(line.strip().split())
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# letters = [i for i in alphabet]
#
# current = 0
# while current > -1 and current < 41:
#     if ins[current][0] == "snd":
#         before = int(reg[ins[current][1]])
#     elif ins[current][0] == "set":
#         if ins[current][2] not in letters:
#             reg[ins[current][1]] = int(ins[current][2])
#         else:
#             reg[ins[current][1]] = reg[ins[current][2]]
#     elif ins[current][1] in reg:
#         if ins[current][0] == "add":
#             if ins[current][2] not in letters:
#                 reg[ins[current][1]] += int(ins[current][2])
#             else:
#                 reg[ins[current][1]] += reg[ins[current][2]]
#         elif ins[current][0] == "mul":
#             if ins[current][2] not in letters:
#                 reg[ins[current][1]] *= int(ins[current][2])
#             else:
#                 reg[ins[current][1]] *= reg[ins[current][2]]
#         elif ins[current][0] == "mod":
#             if ins[current][2] not in letters:
#                 reg[ins[current][1]] %= int(ins[current][2])
#             else:
#                 reg[ins[current][1]] %= reg[ins[current][2]]
#         elif ins[current][0] == "rcv":
#             if reg[ins[current][1]] != 0:
#                 print(before)
#                 break
#                 reg[ins[current][1]] = before
#         elif ins[current][0] == "jgz":
#             if reg[ins[current][1]] > 0:
#                 current += int(ins[current][2]) - 1
#     current += 1

# Answer is first before

# Part 2

file = open("Day18Input.txt", "r")
reg = {}
ins = []
forP0 = []
forP1 = []
id = 0
for line in file:
    ins.append(line.strip().split())

alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = [i for i in alphabet]

deadlock = [False, False]

current = 0
while current > -1 and current < 41:
    deadlock[id] = False
    reg["p"] = id
    if ins[current][0] == "snd":
        if id == 0:
            forP1.append(reg[ins[current][1]])
        else:
            forP0.append(reg[ins[current][1]])
    elif ins[current][0] == "set":
        if ins[current][2] not in letters:
            reg[ins[current][1]] = int(ins[current][2])
        else:
            reg[ins[current][1]] = reg[ins[current][2]]
    elif ins[current][1] in reg:
        if ins[current][0] == "add":
            if ins[current][2] not in letters:
                reg[ins[current][1]] += int(ins[current][2])
            else:
                reg[ins[current][1]] += reg[ins[current][2]]
        elif ins[current][0] == "mul":
            if ins[current][2] not in letters:
                reg[ins[current][1]] *= int(ins[current][2])
            else:
                reg[ins[current][1]] *= reg[ins[current][2]]
        elif ins[current][0] == "mod":
            if ins[current][2] not in letters:
                reg[ins[current][1]] %= int(ins[current][2])
            else:
                reg[ins[current][1]] %= reg[ins[current][2]]
        elif ins[current][0] == "rcv":
            if id == 0:
                if len(forP0) == 0:
                    deadlock[0] = True
                    break
                reg[ins[current][1]] = forP0[0]
                del forP0[0]
            else:
                if len(forP1) == 0:
                    deadlock[1] = True
                    break
                reg[ins[current][1]] = forP1[0]
                del forP1[0]
        elif ins[current][0] == "jgz":
            if reg[ins[current][1]] > 0:
                current += int(ins[current][2]) - 1
    current += 1

print()

