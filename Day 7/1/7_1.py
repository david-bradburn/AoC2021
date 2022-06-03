from setuptools import setup


file = "input.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines() ## [0].strip("\n").split
    input_cleaned = input_raw[0].strip("\n").split(",")
    crab_positions = []
    for i in input_cleaned:
        crab_positions += [int(i)]

def setup_dict(start, end):
    dict_temp = {}
    for i in range(start, end):
        dict_temp[i] = 0
    return dict_temp

crab_max_position = max(crab_positions)
crab_min_position = min(crab_positions)

cost_of_final_position = setup_dict(crab_min_position, crab_max_position)


for x in range(crab_min_position, crab_max_position):
    for crab in crab_positions:
        cost_of_final_position[x] += abs(crab - x)


print(cost_of_final_position)
min_cost_key = min(cost_of_final_position, key=cost_of_final_position.get)
print(cost_of_final_position[min_cost_key])
# print(max(crab_positions))


#356958

