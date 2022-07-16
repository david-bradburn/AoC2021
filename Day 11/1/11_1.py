# First, the energy level of each octopus increases by 1.
# Then, any octopus with an energy level greater than 9 
# flashes. This increases the energy level of all adjacent 
# octopuses by 1, including octopuses that are diagonally 
# adjacent. If this causes an octopus to have an energy 
# level greater than 9, it also flashes. This process 
# continues as long as new octopuses keep having their 
# energy level increased beyond 9. (An octopus can only 
# flash at most once per step.)
# Finally, any octopus that flashed during this step has 
# its energy level set to 0, as it used all of its energy to flash.

import numpy as np

file = "test.txt"

DAY_NO = "11"
PART = "1"

file_path = "Day " + DAY_NO + "/misc/"

board = np.zeros((10, 10), dtype = int)
ones = np.ones((10, 10), dtype = int)
exploded_octopuses = np.zeros((10, 10), dtype = int)
# print(board)
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()
    input_stripped = []
    input_stripped += [i.strip("\n") for i in input_raw]
    input_split = []
    for index_row, row in enumerate(input_stripped):
        for index_octopus, octopus in enumerate(row):
            board[index_row][index_octopus] = octopus


print(board)


def step1(board):
    return board + ones


def step2(board):
    for row_indx, row in enumerate(board):
        for octopus_indx,  in enumerate(row):
            if octopus >= 9 and not board[row_indx][octopus_indx]:
                board[row_indx][octopus_indx] = 1 ## the octopus has now exploded and is now locked?
                
    
# print(input_stripped)