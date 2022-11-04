#################################################################
###### https://adventofcode.com/2021/day/21 #####################
#################################################################

file = "test.txt"

DAY_NO = "21"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readlines()
	player_1_start_raw = input_raw[0].strip('\n')[-1]
	player_2_start_raw = input_raw[1].strip('\n')[-1]

print(player_1_start_raw, player_2_start_raw)

class Dirac_Board():

	def __init__(self) -> None:
		pass

	


