# Part 1

steps = 344 # input
buffer = [0]
new = 1
current = 0
before = 0

# while new < 2018*100:
#     current = (current + steps) % len(buffer)
#     buffer.insert(current + 1, new)
#     current += 1
#     new += 1
#
# print(buffer[current + 1])

# Part 2

answer = 0
for i in range(1, 50000001):
    current = (current + 345) % i
    if current == 0:
        print(i)

# Take last answer