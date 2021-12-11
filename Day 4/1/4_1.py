import numpy as np

with open("../misc/test.txt", "r") as fd:
    input = list(map(int,fd.readline().strip("\n").split(","))) ## turns inputs into an array of ints
    boards = fd.readlines()

boards = [x.strip("\n") for x in boards][1:]
boards = boards + [""]
# print(boards)
boards_proccesed = []
temp = []

cnt = 0

for x in boards:
    print(x)
    if x == "":
        cnt += 1
        boards_proccesed += [temp]
        print(temp)
        temp = []
    else:
        temp += [[i for i in x.split(" ") if i]]
        # temp += [(x.split(" ")).remove("")]

print(cnt)
for i in range(cnt):
    print(boards_proccesed[i])
