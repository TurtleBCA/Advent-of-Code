# Part 1

userInput = input()
sum = 0
for i in range(len(userInput) - 1):
    if userInput[i] == userInput[i+1]:
        sum += int(userInput[i])
if userInput[len(userInput) - 1] == userInput[0]:
    sum += int(userInput[len(userInput) - 1])

print(sum)

# Part 2

sum = 0
for i in range(len(userInput)):
    if userInput[i] == userInput[(i + len(userInput) // 2) % len(userInput)]:
        sum += int(userInput[i])

print(sum)