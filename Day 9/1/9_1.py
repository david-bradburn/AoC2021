

import numpy as np

file = "input.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()
    input_stripped = []
    input_stripped += [i.strip("\n") for i in input_raw]
    # print(input_stripped)
    N = 100
    M = 100
    arr = np.zeros((M, N), dtype =int)
    # print(arr)
    for i in range(M):
        for j in range(N):
            arr[i][j] = input_stripped[i][j]

sea_bed = arr
min_sea_bed = np.ones_like(sea_bed)
# print(sea_bed)
# print(min_sea_bed)
arr_check = [-1, 1]

for y in range(M):
    for x in range(N):
        for vert in arr_check:
            try:
                if sea_bed[y][x + vert] <= sea_bed[y][x]:
                    min_sea_bed[y][x] = 0
            except:
                pass

            try:
                if sea_bed[y + vert][x] <= sea_bed[y][x]:
                    min_sea_bed[y][x] = 0
            except:
                pass
        
                
# print(min_sea_bed)
risk_level = 0
for y in range(M):
    for x in range(N):
        if min_sea_bed[y][x]:
            risk_level += (sea_bed[y][x] + 1)

print(risk_level)

##504


