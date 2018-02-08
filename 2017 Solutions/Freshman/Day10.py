# Part 1

nums = [i for i in range(256)]
skipSize = 0
lengths = []
current = 0
file = open("Day10Input.txt", "r")
for line in file:
    lengths = line.split(",")
    for i in range(len(lengths)):
        lengths[i] = int(lengths[i])
for i in lengths:
    tmp = []
    start = current
    for j in range(i):
        tmp.append(nums[current])
        current = (current + 1) % 256
    tmp.reverse()
    for j in range(i):
        nums[(start + j) % 256] = tmp[j]
    current = (current + skipSize) % 256
    skipSize += 1
print(nums[0] * nums[1])

# Part 2

nums = [i for i in range(256)]
skipSize = 0
lengths = []
extraLengths = [17, 31, 73, 47, 23]
current = 0


file = open("Day10Input.txt", "r")
for line in file:
    tmpLengths = line.split(",")
    for i in range(len(tmpLengths)):
        total = ""
        for j in tmpLengths[i]:
            lengths.append(ord(j))
        lengths.append(44)
lengths = lengths[:-1]
for i in extraLengths:
    lengths.append(i)
print(lengths)

for r in range(64):
    for i in lengths:
        tmp = []
        start = current
        for j in range(i):
            tmp.append(nums[current])
            current = (current + 1) % 256
        tmp.reverse()
        for j in range(i):
            nums[(start + j) % 256] = tmp[j]
        current = (current + skipSize) % 256
        skipSize += 1

print(nums)

startFrom = 0
finalList = []
finalElement = ""
for i in range(16):
    tmp = nums[startFrom:startFrom + 16]
    cumulative = tmp[0] ^ tmp[1]
    for j in tmp[2:]:
        cumulative ^= j
    startFrom += 16

    finalElement = str(hex(cumulative)[2:])
    if len(finalElement) == 2:
        finalList.append(finalElement)
    else:
        finalList.append("0" + finalElement)
print(finalList)

final = ""
for i in finalList:
    final += i
print(final)
print(len(final))

# Answer is not 8b646deaa9ad821dbce9bb3c5d780ae
# Answer is not 8b646dea0a9ad821dbce9bb3c5d780ae
# Nums is not [153, 204, 144, 240, 229, 7, 126, 65, 137, 195, 94, 251, 90, 224, 227, 213, 181, 40, 106, 58, 169, 70, 63, 22, 11, 60, 159, 110, 241, 98, 174, 148, 162, 100, 35, 78, 147, 13, 123, 209, 23, 131, 62, 104, 101, 82, 156, 155, 170, 177, 207, 183, 219, 167, 143, 176, 161, 103, 118, 186, 1, 130, 30, 93, 105, 80, 245, 202, 253, 134, 97, 139, 53, 226, 192, 128, 21, 15, 200, 216, 189, 184, 24, 205, 152, 28, 87, 252, 45, 217, 33, 37, 249, 117, 54, 47, 17, 138, 135, 25, 76, 56, 48, 246, 193, 142, 119, 165, 211, 218, 71, 188, 164, 111, 20, 91, 254, 16, 19, 27, 51, 32, 175, 57, 163, 233, 83, 223, 220, 95, 120, 178, 84, 187, 74, 89, 8, 55, 26, 199, 125, 67, 112, 194, 81, 247, 66, 96, 43, 225, 146, 92, 221, 234, 4, 114, 243, 222, 242, 208, 12, 197, 231, 121, 88, 149, 230, 3, 44, 107, 248, 102, 206, 179, 236, 172, 10, 198, 180, 14, 244, 168, 237, 0, 64, 6, 212, 238, 140, 116, 73, 185, 133, 173, 52, 38, 59, 31, 86, 5, 191, 72, 166, 127, 99, 50, 115, 132, 151, 39, 69, 136, 141, 124, 232, 145, 150, 61, 255, 68, 18, 239, 235, 36, 201, 171, 182, 109, 157, 250, 214, 29, 42, 190, 154, 203, 46, 34, 9, 85, 75, 160, 108, 122, 79, 2, 129, 158, 113, 210, 215, 228, 49, 196, 41, 77]
# Answer is not d395f81cf7040feeb2b79527e131895e
# Lengths is not [5752, 5652, 48, 5557, 50, 5055, 5649, 49, 495051, 5751, 504956, 5051, 494851, 505353, 505352, 17, 31, 73, 47, 23]
# Nums is not [12, 38, 159, 53, 87, 21, 71, 181, 188, 33, 92, 102, 56, 11, 234, 157, 158, 73, 179, 213, 68, 202, 247, 63, 183, 184, 34, 215, 14, 174, 84, 108, 58, 61, 192, 142, 28, 111, 252, 178, 176, 238, 17, 236, 107, 149, 110, 191, 144, 48, 112, 167, 103, 139, 16, 180, 143, 205, 245, 104, 101, 132, 220, 193, 151, 138, 52, 189, 203, 85, 66, 94, 230, 44, 75, 229, 124, 89, 141, 45, 243, 200, 162, 210, 83, 231, 216, 117, 206, 250, 164, 254, 90, 131, 133, 100, 76, 4, 99, 194, 30, 241, 228, 172, 160, 29, 35, 148, 130, 129, 115, 59, 209, 161, 177, 86, 0, 249, 36, 39, 32, 113, 72, 47, 233, 79, 248, 235, 195, 163, 20, 207, 153, 13, 137, 125, 135, 165, 171, 227, 96, 226, 18, 147, 246, 19, 106, 201, 170, 251, 223, 166, 168, 240, 150, 82, 152, 217, 190, 186, 136, 218, 26, 6, 69, 214, 23, 49, 40, 50, 118, 197, 5, 116, 212, 98, 46, 196, 74, 114, 93, 15, 182, 121, 120, 77, 204, 91, 175, 27, 119, 9, 211, 221, 8, 169, 70, 145, 127, 173, 1, 225, 109, 199, 232, 62, 134, 81, 57, 253, 242, 140, 25, 95, 2, 239, 60, 128, 22, 185, 198, 88, 154, 55, 10, 80, 126, 105, 222, 237, 37, 41, 244, 54, 78, 97, 42, 64, 156, 224, 43, 3, 51, 7, 219, 155, 65, 67, 255, 146, 24, 122, 208, 123, 187, 31]