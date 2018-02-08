steps = 12861455
state = "A"
tape = [0]

current = 0

def moveRight():
    global current
    if current == len(tape) - 1:
        current = len(tape)
        tape.append(0)
    else:
        current += 1

def moveLeft():
    global current
    if current == 0:
        tape.insert(0, 0)
    else:
        current -= 1

for i in range(steps):
    if state == "A":
        if tape[current] == 0:
            tape[current] = 1
            moveRight()
            state = "B"
        else:
            tape[current] = 0
            moveLeft()
            state = "B"
    elif state == "B":
        if tape[current] == 0:
            tape[current] = 1
            moveLeft()
            state = "C"
        else:
            tape[current] = 0
            moveRight()
            state = "E"
    elif state == "C":
        if tape[current] == 0:
            tape[current] = 1
            moveRight()
            state = "E"
        else:
            tape[current] = 0
            moveLeft()
            state = "D"
    elif state == "D":
        if tape[current] == 0:
            tape[current] = 1
            moveLeft()
            state = "A"
        else:
            tape[current] = 1
            moveLeft()
            state = "A"
    elif state == "E":
        if tape[current] == 0:
            tape[current] = 0
            moveRight()
            state = "A"
        else:
            tape[current] = 0
            moveRight()
            state = "F"
    elif state == "F":
        if tape[current] == 0:
            tape[current] = 1
            moveRight()
            state = "E"
        else:
            tape[current] = 1
            moveRight()
            state = "A"

count = 0
for i in tape:
    if i == 1:
        count += 1

print(count)