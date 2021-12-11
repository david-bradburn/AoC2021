
list = []
gamma = ''
epilson = ''
one = 0

with open("../misc/input.txt", "r") as fd:
    for line in fd:
        list += [line.strip('\n')]

half = len(list)/2
for i in range(len(list[0])):
    one = 0
    for j in range(len(list)):
        if list[j][i] == '1':
            one += 1

    if one > half:
        gamma += '1'
        epilson += '0'
    elif one < half:
        gamma += '0'
        epilson += '1'
    else:
        print("Error")

print(int(gamma, 2))
print(int(epilson, 2))
print((int(gamma, 2)) * int(epilson, 2))