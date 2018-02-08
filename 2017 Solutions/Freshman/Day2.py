# Part 1

file = open("Day2Input.txt", "r")
sum = 0
for line in file:
    numbers = line.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    sum += max(numbers) - min(numbers)

print(sum)

# Part 2

file = open("Day2Input.txt", "r")
sum = 0
for line in file:
    numbers = line.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    numbers.sort()
    for i in range(len(numbers)):
        j = i + 1
        while j < len(numbers):
            if numbers[j] % numbers[i] == 0:
                sum += numbers[j] / numbers[i]
                break
            j += 1
print(sum)