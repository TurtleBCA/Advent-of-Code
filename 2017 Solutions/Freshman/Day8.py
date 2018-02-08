file = open("Day8Input.txt", "r")
dict = {}
greatest = 0
for line in file:
    lineList = line.strip().split()
    lineList[2] = int(lineList[2])
    lineList[6] = int(lineList[6])
    print(lineList)
    if lineList[5] == "<":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] < lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == ">":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] > lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == "<=":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] <= lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == ">=":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] >= lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == "==":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] == lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == "!=":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] != lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]

keys = list(dict.keys())
greatest = 0
for i in keys:
    if dict[i] > greatest:
        greatest = dict[i]

print(greatest)

# Part 2

file = open("Day8Input.txt", "r")
dict = {}
for line in file:
    lineList = line.strip().split()
    lineList[2] = int(lineList[2])
    lineList[6] = int(lineList[6])
    print(lineList)
    if lineList[5] == "<":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] < lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == ">":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] > lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == "<=":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] <= lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == ">=":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] >= lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == "==":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] == lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]
    elif lineList[5] == "!=":
        dict[lineList[4]] = dict.get(lineList[4], 0)
        if dict[lineList[4]] != lineList[6]:
            dict[lineList[0]] = dict.get(lineList[0], 0)
            if lineList[1] == "inc":
                dict[lineList[0]] += lineList[2]
            else:
                dict[lineList[0]] -= lineList[2]

    keys = list(dict.keys())
    for i in keys:
        if dict[i] > greatest:
            greatest = dict[i]

print(greatest)