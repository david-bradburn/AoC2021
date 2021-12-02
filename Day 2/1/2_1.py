depth = 0
forward = 0
instr = []
with open("../misc/input.txt", "r") as fd:
    for line in fd:
        instr = line.split()
        match instr[0]:
            case 'forward' : forward += int(instr[1])
            case 'up' : depth -= int(instr[1])
            case 'down' : depth += int(instr[1])
            case '_' : print("error")

print(depth)
print(forward)
print(forward*depth)