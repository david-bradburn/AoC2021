
sum_prev = 10000
cnt = 0
depth_array = []
with open("../misc/input.txt", "r") as fd:
    for line in fd:
        depth_array += [int(line)]

for i in range(len(depth_array)):
    try:
        sum = depth_array[i] + depth_array[i+1] + depth_array[i+2]
        if sum > sum_prev:
            cnt += 1
        sum_prev = sum
    except IndexError:
        print(cnt)
##1748