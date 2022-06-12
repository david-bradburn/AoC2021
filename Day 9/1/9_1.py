

import numpy as np

file = "test.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()
    input_stripped = []
    input_stripped += [i.strip("\n") for i in input_raw]
    # print(input_stripped)
    N = 10
    M = 5
    arr = np.zeros((M, N), dtype =int)
    # print(arr)
    for i in range(M):
        for j in range(N):
            arr[i][j] = input_stripped[i][j]

sea_bed = arr
min_sea_bed = np.zeros_like(sea_bed)
print(sea_bed)

for y in range(M):
    for x in range(N):
        cells_to_check = []
        match x, y:
            case (0, 0):
                cells_to_check = [[x + 1, y], [x, y + 1]]
            case (0, z) if z != N: ### draw a diagram
                cells_to_check = [[x + 1, y], [x, y + 1]]




