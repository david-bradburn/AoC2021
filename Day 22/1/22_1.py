#################################################################
###### https://adventofcode.com/2021/day/22 #####################
#################################################################

file = "test1.txt"

DAY_NO = "22"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

flip_arr = []
coords_clean = []

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()
	
	for row in raw_input:
		temp = row.strip('\n').split(' ')
		
		match temp:
			case [on_off, coords_raw]:
				print(on_off)
				match on_off:
					case "on":
						flip_arr += [1]
					case "off":
						flip_arr += [0]
				
				# print(coords_raw.split(','))
				temp_arr = []
				for n, cd in enumerate(coords_raw.split(',')):

					start1 = cd.find("=")
					end1 = cd.find(".")
					coord_st = int(cd[start1+1:end1])
					coord_end = int(cd[end1+2:])

					temp_arr += [[coord_st, coord_end]]
					# print(coord_st, coord_end)
				
				coords_clean += [temp_arr]

					



			case _:
				raise Exception("Yeah nah this aint meant to look like this")


print(flip_arr)
print(coords_clean)
for i in coords_clean:
	print(i)
