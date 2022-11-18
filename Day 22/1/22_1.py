#################################################################
###### https://adventofcode.com/2021/day/22 #####################
#################################################################

file = "test1.txt"

DAY_NO = "22"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()
	test = []
	for row in raw_input:
		temp = row.strip('\n').split(' ')
		
		match temp:
			case [on_off, coord]:
				print(on_off)
				print(coord.split(','))


