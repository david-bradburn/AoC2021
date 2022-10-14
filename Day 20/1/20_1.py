#################################################################
###### https://adventofcode.com/2021/day/20 #####################
#################################################################


import numpy as np

file = "test.txt"

DAY_NO = "20"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readlines()

iea_raw = input_raw[0].strip('\n')
iea_str = ''
for i in iea_raw:
	match i:
		case '#':
			iea_str += '1'
		case '.':
			iea_str += '0'
		
		case _:
			raise TypeError

# print(iea_str)
board_raw = input_raw[2:]
board_stripped = [i.strip("\n") for i in board_raw]
# print(board_stripped)
height = len(board_stripped)
width = len(board_stripped[0])

No_of_runs = 2
padding  = 2 * No_of_runs

board = np.zeros((width + padding, height + padding), dtype=int)
# print(board)
for row_index, row in enumerate(board_stripped):
	for column_index, item in enumerate(row):
		match item:
			case('#'):
				board[No_of_runs+row_index][No_of_runs+column_index] = 1
			case('.'):
				board[No_of_runs+row_index][No_of_runs+column_index] = 0
			case _:
				raise TypeError
		
		
print(board)

class Image:

	def __init__(self, board) -> None:
		self.board = board
	
		


# print(iea)
# print(1)