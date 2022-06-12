import numpy as np


file = "test.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()
    input_stripped = []
    input_stripped += [i.strip("\n") for i in input_raw]
    print(input_stripped)
    N = 10
    M = 5
    arr = np.zeros((M, N), dtype =int)
    # print(arr)
    for i in range(M):
        for j in range(N):
            arr[i][j] = input_stripped[i][j]

print(arr)