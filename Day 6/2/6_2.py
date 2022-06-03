# import numpy as np

NO_OF_DAYS = 256
file = "input.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()[0].strip("\n").split(",")
    input_cleaned = []
    for i in input_raw:
        input_cleaned += [int(i)]

print(input_cleaned)

fishes = input_cleaned
## turn thr array into a dictionary
def clear_fish_dict():
    fish_dict_temp = {}
    for i in range(9):
        fish_dict_temp[i] = 0
    return fish_dict_temp

def total_fish_count(fish_dict : dict):
    cnt = 0
    for key in fish_dict:
        cnt += fish_dict[key]
    return cnt

fish_dict = {}
fish_dict_temp = {}
for i in range(9):
    fish_dict[i] = 0
    fish_dict_temp[i] = 0

# print(fish_dict)
for fish in fishes:
    fish_dict[fish] += 1

print(fish_dict)

for i in range(NO_OF_DAYS):
    print("Day {}".format(i + 1))
    fish_dict_temp = clear_fish_dict()
    for fish in fish_dict:
        match fish:
            case 0:
                fish_dict_temp[6] += fish_dict[0]
                fish_dict_temp[8] = fish_dict[0]
            case ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 ):
                fish_dict_temp[fish - 1] += fish_dict[fish]

    fish_dict = fish_dict_temp

print(total_fish_count(fish_dict))

## 1595330616005
