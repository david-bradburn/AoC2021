

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

## the code above is just to clean the input

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
# this finds the local minima on the sea bed            

## need to create dictionary of points that have a local minima
local_minima_dict = {}
for index, value in np.ndenumerate(min_sea_bed):
    if(value):
        local_minima_dict[index] = 0
        # print(index)
        # print(local_minima_dict)

direction_arr_master = np.array(["up", "right", "down", "left"])


def local_min_finder(arr, current_index, current_direction_arr, route):
    # print(current_direction_arr)
    if current_index in local_minima_dict:
        return current_index
    else:
        y = current_index[0]
        x = current_index[1]
        for direction in current_direction_arr:
            # print(y, x)
            # print(direction)
            match direction:
                case "up":
                    if y - 1 < 0:
                        continue
                    if arr[y - 1][x] < arr[y][x]:
                        route += [direction, (y-1,x)]
                        return local_min_finder(arr, (y-1,x), np.delete(direction_arr_master, 2), route)
                
                case "right":

                    if x + 1 > N - 1:
                        continue
                    if arr[y][x + 1] < arr[y][x]:
                        route += [direction, (y,x + 1)]
                        # print(route)
                        return local_min_finder(arr, (y, x + 1), np.delete(direction_arr_master, 3), route)


                case "down":
                    if y + 1 > M - 1:
                        continue
                    if arr[y + 1][x] < arr[y][x]:
                        route += [direction, (y+1,x)]
                        return local_min_finder(arr, (y + 1, x), np.delete(direction_arr_master, 0), route)
                
                case "left":
                    
                    if x - 1 < 0:
                        continue
                    if arr[y][x - 1] < arr[y][x]:
                        route += [direction, (y,x - 1)]
                        return local_min_finder(arr, (y, x - 1), np.delete(direction_arr_master, 1), route)



print(sea_bed)
# print(local_minima_dict)
for index, value in np.ndenumerate(sea_bed):
    if value == 9:
        continue

    route = [index]
    local_min = local_min_finder(sea_bed, index, direction_arr_master, route)
    if local_min == None:
        print(index, value, "->", local_min)
        print("Route", route)

    if (local_min in local_minima_dict):
        local_minima_dict[local_min] += 1
    else:
        print(local_min)
        print("ERROR NOT LOCAL MINIMA")

# print(local_minima_dict)    
size_list = []
for key in local_minima_dict:
    size_list += [local_minima_dict[key]]

print(size_list)
max1 = max(size_list)
size_list.remove(max1)
print(max1)
max2 = max(size_list)
print(max2)
size_list.remove(max2)
max3 = max(size_list)
size_list.remove(max3)

print(max1, max2, max3)
print(max1 * max2 * max3)

## 1558722





