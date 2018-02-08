banks = input().split()

for i in range(len(banks)):
    banks[i] = int(banks[i])

already = []
steps = 0

while banks not in already:
    tmp = []
    for i in banks:
        tmp.append(i)
    already.append(tmp)

    blocks = max(banks)
    original = banks.index(blocks)
    banks[original] = 0

    currentIndex = (original + 1) % 16
    while blocks > 0:
        banks[currentIndex] += 1
        blocks -= 1
        currentIndex = (currentIndex + 1) % 16
    steps += 1

print(steps)

# Part 2
first = already.index(banks)
print(steps - first)