# Part 1

#  file = open("Day23Input.txt", "r")
# reg = {}
# ins = []
#
# registers = "abcdefgh"
# for i in registers:
#     reg[i] = 0
#
# for line in file:
#     ins.append(line.strip().split())
#
# current = 0
# counter = 0
# while current > -1 and current < 32:
#     ins0 = ins[current][0]
#     ins1 = ins[current][1]
#     ins2 = ins[current][2]
#     if ins0 == "set":
#         reg[ins1] = reg.get(ins2) or int(ins2)
#     elif ins0 == "sub":
#         reg[ins1] -= reg.get(ins2) or int(ins2)
#     elif ins0 == "mul":
#         reg[ins1] *= reg.get(ins2) or int(ins2)
#         counter += 1
#     elif ins0 == "jnz":
#         if reg.get(ins1) != 0:
#             current += int(ins2) - 1
#     current += 1
#
# print(counter)

# Part 2

# file = open("Day23Input.txt", "r")
# reg = {}
# ins = []
#
# registers = "abcdefgh"
# for i in registers:
#     reg[i] = 0
#
# reg["a"] = 1
# reg["b"] = 0
# reg["c"] = 0
# reg["d"] = 0
# reg["e"] = 0
# reg["g"] = 0
# reg["h"] = 0
#
# for line in file:
#     ins.append(line.strip().split())
#
# current = 0
# while current > -1 and current < 32:
#     ins0 = ins[current][0]
#     ins1 = ins[current][1]
#     ins2 = ins[current][2]
#     print(reg)
#     print(ins[current])
#     if ins0 == "set":
#         reg[ins1] = reg.get(ins2) or int(ins2)
#     elif ins0 == "sub":
#         reg[ins1] -= reg.get(ins2) or int(ins2)
#     elif ins0 == "mul":
#         reg[ins1] *= reg.get(ins2) or int(ins2)
#     elif ins0 == "jnz":
#         if reg.get(ins1) != 0:
#             current += int(ins2) - 1
#     current += 1
#     if reg["e"] == 200:
#         break
#
# print(reg["h"])

# Not 1000 (answer is too high)

b = 106700
c = 123700
d = 2
e = 2
h = 0

for i in range(106700, 123700, 17):
    b = i
    f = 1
    d = 2
    e = 2
    while True:
        if d * e - b == 0:
            f = 0
        e += 1
        if e - b != 0:
            continue
        else:
            d += 1
            if d - b != 0:
                break
            else:
                if f == 0:
                    h += 1
    print(b)

print(h)