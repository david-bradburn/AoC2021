import numpy as np

class Sea_Floor:
    def __init__(self):
        self.height = 1000
        self.width = 1000
        self.sea_floor_arr = np.zeros((self.width, self.height), dtype=int)
        self.no_of_dangerous_coords = 0

    def __return_ordered_starting_point_and_delta(self, val1, val2):
        if val1 > val2:
            assert(val1 - val2 >=0)
            return val1, val2, val1 - val2
        else:
            assert(val2 - val1 >=0)
            return val2, val1, val2 - val1

    def vent(self, start_x, start_y, end_x, end_y):
        end_x, start_x, delta_x_pos = self.__return_ordered_starting_point_and_delta(start_x, end_x)
        end_y, start_y, delta_y_pos = self.__return_ordered_starting_point_and_delta(start_y, end_y)
        if (delta_x_pos != 0) ^ (delta_y_pos != 0):
            for dx in range(delta_x_pos + 1):
                for dy in range(delta_y_pos + 1):
                    self.sea_floor_arr[start_y + dy][start_x + dx] += 1
        # print(self.sea_floor_arr)

        # self.find_dangerous_areas()
    
    def find_dangerous_areas(self, dangerous_thres = 2):
        cnt = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.sea_floor_arr[y][x] >= dangerous_thres:
                    cnt += 1
        self.no_of_dangerous_coords = cnt




with open("../misc/input.txt", "r") as fd:
    input_raw = fd.readlines() ##.strip("\n").split("->")
    # for i in input_raw:
    input_striped = []
    input_cleaned_str = []
    temp = []
    for i in input_raw:
        input_striped += [i.strip('\n').split('->')]
    for index_1 in input_striped:
        temp = []
        for index_2 in index_1:
            # print(index_2)
            temp += [index_2.strip(' ').split(',')]
        input_cleaned_str += [temp]
    
    for i in range(len(input_cleaned_str)):
        for j in range(len(input_cleaned_str[i])):
            for k in range(len(input_cleaned_str[i][j])):
                input_cleaned_str[i][j][k] = int(input_cleaned_str[i][j][k])
    

print(input_cleaned_str)
sea_floor = Sea_Floor()

# print(len(input_cleaned_str[0]))
for vent_coord in input_cleaned_str:
    sea_floor.vent(vent_coord[0][0], vent_coord[0][1], vent_coord[1][0], vent_coord[1][1])

print(sea_floor.sea_floor_arr)
sea_floor.find_dangerous_areas()
print(sea_floor.no_of_dangerous_coords)

#6841