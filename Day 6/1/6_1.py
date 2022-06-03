# import numpy as np

NO_OF_DAYS = 80
file = "input.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()[0].strip("\n").split(",")
    input_cleaned = []
    for i in input_raw:
        input_cleaned += [int(i)]

print(input_cleaned)

arr_of_fishes = input_cleaned
for i in range(NO_OF_DAYS):
    new_arr_of_fishes = []
    for fish in arr_of_fishes:
        if fish == 0:
            new_arr_of_fishes += [6, 8]
        else:
            new_arr_of_fishes += [fish - 1]

    arr_of_fishes = new_arr_of_fishes

print(len(arr_of_fishes))