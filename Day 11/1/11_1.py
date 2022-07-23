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

file = "input.txt"

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


def increaseEnergyLevel(board):
    return board + ones


COORDS = [(-1, -1), (-1,  0), (-1,  1),
         ( 0, -1),           ( 0,  1),
         ( 1, -1), ( 1,  0), ( 1,  1)]

def explodeOctopus(board_i):
    past_flashes = None
    flashes = 0
    exploded_octopuses = np.zeros((10, 10), dtype = int)
    while past_flashes != flashes:
        past_flashes = flashes
        for row_indx, row in enumerate(board_i):
            for octopus_indx, octopus in enumerate(row):
                # print(octopus)
                if octopus > 9 and not exploded_octopuses[row_indx][octopus_indx]:
                    flashes += 1
                    # print("Octopus flashes")
                    exploded_octopuses[row_indx][octopus_indx] = 1 ## the octopus has now exploded and is now locked?
                    board_i[row_indx][octopus_indx] = 0
                    for x, y in COORDS:
                        new_y = row_indx + y
                        new_x = octopus_indx + x
                        in_bounds_x = new_x >= 0 and new_x < 10
                        in_bounds_y = new_y >= 0 and new_y < 10
                        if in_bounds_x and in_bounds_y and not exploded_octopuses[new_y][new_x]:
                            board_i[new_y][new_x] += 1

    return board_i, flashes

no_of_flashes = 0
NO_OF_STEPS = 100
for i in range(NO_OF_STEPS):
    board = increaseEnergyLevel(board)
    board, temp_flashes = explodeOctopus(board)
    no_of_flashes += temp_flashes
    print("After Step {}".format(i + 1))
    print(board)
    print("No of flashes {}".format(no_of_flashes))



##  1681