# Part 1

file = open("Day4Input.txt", "r")
counter = 0
for line in file:
    already = []
    valid = True
    words = line.split()
    for word in words:
        if not (word in already):
            already.append(word)
        else:
            valid = False
            break
    if valid == True:
        counter += 1
print(counter)

# Part 2

file = open("Day4Input.txt", "r")
counter = 0
for line in file:
    already = [{}]
    valid = True
    words = line.split()
    for word in words:
        tmpSet = {}
        for letter in word:
            tmpSet[letter] = tmpSet.get(letter, 0) + 1
        for set in already:
            if set == tmpSet:
                valid = False
                break

        already.append(tmpSet)
    if valid == True:
        counter += 1
print(counter)