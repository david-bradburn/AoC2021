import numpy as np

file = "input.txt"

DAY_NO = "13"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readlines()
	input_stripped = []
	input_stripped += [i.strip("\n").split(",") for i in input_raw]
	coords = []
	commands = []
	max_y = 0
	max_x = 0
	for i in input_stripped:
		if len(i) == 2:
			coords += [[int(i[0]), int(i[1])]]
			if coords[-1][0] > max_x:
				max_x = coords[-1][0]
			if coords[-1][1] > max_y:
				max_y = coords[-1][1]
		elif i[0] == '':
			pass
		else: 
			match i[0].split("="):
				case ["fold along y", y]:
					commands += [["y", int(y)]]
				case ["fold along x", x]:
					commands +=[["x", int(x)]]
				case _:
					print("Pattern matching didn't work")

# print(coords)
# print(commands)

# ## find the max coords - done
# print(max_x, max_y)
##create the paper
paper = np.zeros((max_y +1, max_x + 1), dtype= int)
# print(paper)

##get the points on the paper


for coord in coords:
	paper[coord[1]][coord[0]] = 1

print(paper)

for command in commands:
	match command[0]:
		case "x":
			# print(type(command[1]))
			new_paper = paper[:,:command[1]]
			paper_to_fold = np.fliplr(paper[:, command[1]+1:])
			
			# print(new_paper)
			# print(paper_to_fold)
			print(paper.shape)
			folded_paper = np.pad(paper_to_fold, ((0,0),(new_paper.shape[0]- paper_to_fold.shape[0],0)), 'constant', constant_values=0)
			paper = new_paper | folded_paper
			print(paper)
		case "y":
			# print(type(command[1]))
			new_paper = paper[:command[1],:]
			paper_to_fold = np.flipud(paper[command[1]+1:, :])
			
			# print(new_paper)
			# print(paper_to_fold)
			print(paper.shape)
			folded_paper = np.pad(paper_to_fold, ((new_paper.shape[0]- paper_to_fold.shape[0],0),(0,0)), 'constant', constant_values=0)
			paper = new_paper | folded_paper
			print(paper)



for row in paper:
	row_str = ""
	for char in row:
		if(char):
			row_str += " #"
		else:
			row_str += "  "
	print(row_str)

## LRGPRECB
