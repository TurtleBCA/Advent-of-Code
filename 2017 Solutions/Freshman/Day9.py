# Part 1

file = open("Day9Input.txt", "r")
canceled = []
for line in file:
    lineList = list(line)
    for index in range(len(lineList)):
        if lineList[index] == "!":
            lineList[index] = " "
            lineList[index + 1] = " "
    canceled = lineList
    while " " in canceled:
        canceled.remove(" ")

print(canceled)

garbage = False
cleaned = []
count = 0
for index in range(len(canceled)):
    if canceled[index] == ">":
        garbage = False
        canceled[index] = " "
    if garbage == True:
        canceled[index] = " "
        count += 1
        continue
    if canceled[index] == "<":
        garbage = True
        canceled[index] = " "

cleaned = canceled
while " " in cleaned:
    cleaned.remove(" ")
print(cleaned)

score = 0
tier = 0

for i in cleaned:
    if i == "{":
        tier += 1
    elif i == "}":
        score += tier
        tier -= 1
print(score)

# Part 2
print(count)