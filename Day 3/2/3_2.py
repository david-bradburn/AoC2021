
list = []
list2 = []
new_list = []
gamma = ''
epilson = ''
one = 0

with open("../misc/input.txt", "r") as fd:
    for line in fd:
        list += [line.strip('\n')]
        list2 += [line.strip('\n')]


def most_common(array, index, preference): ## preference 1 is for ox, 0 is for C02
    cnt1 = 0
    cnt0 = 0
    print("length of array: {}".format (len(array)))
    print("index in array: {}".format(index))
    print(array)
    for j in range(len(array)):
        # print(j)
        if array[j][index] == '1':
            cnt1 += 1
        elif array[j][index] == '0':
            cnt0 += 1
        else:
            print("ERROR")
    print("1 count is : {}".format(cnt1))
    print("0 count is : {}".format(cnt0))

    if cnt1 > cnt0:
        return "1"
    elif cnt0 > cnt1:
        return "0"
    else:
        return "1"



print(len(list))
print(len(list[0]))
##oxygen generator rate

for n in range(len(list[0])):
    most_common_index = most_common(list, n, 1)
    print("most common is {}".format(most_common_index))
    list = [x for x in list if (x[n] == most_common_index)]
    # print(len(list))
    if len(list) == 1:
        break

ox = int(list[0], 2)
print(ox)

print("-----------------------------------------------")

## CO2 scrubber rating
for n in range(len(list2[0])):
    most_common_index = most_common(list2, n, 1)
    print("most common is {}".format(most_common_index))
    list2 = [x for x in list2 if (x[n] != most_common_index)]
    # print(len(list))
    if len(list2) == 1:
        break

c02 = int(list2[0], 2)
print(c02)

print(ox*c02)

##4672151
