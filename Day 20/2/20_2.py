#################################################################
###### https://adventofcode.com/2021/day/20 #####################
#################################################################



import numpy as np

file = "test.txt"

DAY_NO = "20"
PART = "2"

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

infite_void_value = 0
infite_void_index = 0


print(iea_str)
board_raw = input_raw[2:]
board_stripped = [i.strip("\n") for i in board_raw]
# print(board_stripped)
height = len(board_stripped)
width = len(board_stripped[0])

No_of_runs = 50
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
		self.new_board = np.zeros_like(self.board)
		self.infite_void_value = 0

		self.main()


	def step(self):
		for row_index, row in enumerate(self.new_board):
			for column_index, item in enumerate(row):
				iea_index_str = ''
				for d_row in range(-1, 2, 1):
					for d_col in range(-1, 2, 1):
						try:
							iea_index_str += str(self.board[row_index + d_row][column_index + d_col])
						except IndexError:
							iea_index_str += str(self.infite_void_value)
				
				# print(row_index, column_index)
				# print(iea_index_str)
				iea_index = int(iea_index_str, 2)
				# print(iea_index, int(iea_str[iea_index]))
		
				self.new_board[row_index][column_index] = int(iea_str[iea_index])
			# print('----------------------------')
		new_infite_void_index = ''
		for i in range(9):
			new_infite_void_index += str(self.infite_void_value)
		new_infite_void_index_int = int(new_infite_void_index, 2)
		self.infite_void_value = int(iea_str[new_infite_void_index_int])
		print(self.new_board)

	def count(self):
		temp = 0
		for row in self.new_board:
			for item in row:
				temp += item
		
		print(temp)

	def main(self):
		for i in range(No_of_runs):
			self.step()
			self.count()
			self.board = self.new_board
			self.new_board = np.zeros_like(self.new_board)

	


board_c = Image(board)

# np.set_printoptions(threshold = np.inf)
# np.savetxt('test.txt', board_c.board, fmt='%u')

#17987