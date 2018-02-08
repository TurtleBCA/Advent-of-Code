# Part 2

file = open("Day5Input.txt", "r")
numbers = []
for line in file:
    numbers.append(int(line))
print(numbers)

currentIndex = 0
steps = 0
while currentIndex < len(numbers):
    if numbers[currentIndex] >= 3:
        numbers[currentIndex] -= 1
        currentIndex += numbers[currentIndex] + 1
    else:
        numbers[currentIndex] += 1
        currentIndex += numbers[currentIndex] - 1
    steps += 1

print(steps)