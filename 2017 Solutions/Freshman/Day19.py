file = open("Day19Input.txt")
lines = []
for line in file:
    lines.append([i for i in line])

for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    lines[i] += [" "] * (201 - len(lines[i]))

for i in lines:
    print(i)

current = [0, lines[0].index("|")]

direction = "s"
letters = []

steps = 1
while lines[current[0]][current[1]] != "Y":
    if lines[current[0]][current[1]] == "+":
        if direction == "s":
            direction = "e" if lines[current[0]][current[1] + 1] == "-" else "w"
        elif direction == "e":
            direction = "n" if lines[current[0] - 1][current[1]] == "|" else "s"
        elif direction == "n":
            direction = "w" if lines[current[0]][current[1] - 1] == "-" else "e"
        elif direction == "w":
            direction = "s" if lines[current[0] + 1][current[1]] == "|" else "n"
    if lines[current[0]][current[1]].isalpha():
        letters.append(lines[current[0]][current[1]])
    if direction == "s":
        current[0] += 1
    elif direction == "e":
        current[1] += 1
    elif direction == "n":
        current[0] -= 1
    elif direction == "w":
        current[1] -= 1
    steps += 1

letters += ["Y"]
final = ""
for i in letters:
    final += i
print(final)
print(steps)
# Answer is not 17227