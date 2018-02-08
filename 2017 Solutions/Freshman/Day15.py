# # Part 1
# file = open("Day15Input.txt", "r")
# g1 = int(file.readline().strip()[-3:])
# g2 = int(file.readline().strip()[-3:])
#
# counter = 0
#
# for i in range(40000000):
#     g1 *=  16807
#     g2 *= 48271
#
#     g1 %= 2147483647
#     g2 %= 2147483647
#
#     g1Bin = str(bin(g1))[2:][-16:].zfill(16)
#     g2Bin = str(bin(g2))[2:][-16:].zfill(16)
#
#     if g1Bin == g2Bin:
#         counter += 1
#
#
# print(counter)

# Part 2
file = open("Day15Input.txt", "r")
g1 = int(file.readline().strip()[-3:])
g2 = int(file.readline().strip()[-3:])
counter = 0
g1Val = []
g2Val = []
while min(len(g1Val), len(g2Val)) != 5000000:
    g1 *=  16807
    g2 *= 48271
    g1 %= 2147483647
    g2 %= 2147483647
    if g1 % 4 == 0:
        g1Val.append(str(bin(g1))[2:][-16:].zfill(16))
    if g2 % 8 == 0:
        g2Val.append(str(bin(g2))[2:][-16:].zfill(16))
    print(min(len(g1Val), len(g2Val)))
for i in range(min(len(g1Val), len(g2Val))):
    if g1Val[i] == g2Val[i]:
        counter += 1
print(counter)

# Not 34
# 309