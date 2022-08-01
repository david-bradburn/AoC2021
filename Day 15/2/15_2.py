import math
import numpy as np
from time import time


file = "input.txt"

DAY_NO = "15"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readlines()
	input_stripped = [line.strip("\n") for line in input_raw]
	max_x = len(input_stripped[0])
	max_y = len(input_stripped)
	
	assert max_x == max_y
	cavern1 = np.zeros((max_x, max_y), dtype=int)
	risk_adder_arr = np.ones((max_x, max_y), dtype=int)
	cavern_all = np.zeros((5*max_x, 5*max_y), dtype=int)
	for row_index, row in enumerate(input_stripped):
		for value_index, value in enumerate(row):
			cavern1[row_index][value_index] = value
	
	for row_index, row in enumerate(cavern_all):
		for column_index, value in enumerate(row):
			row_adder = row_index // max_x
			column_adder = column_index // max_y

			cavern_old_row_index =  row_index % max_x
			cavern_old_column_index = column_index % max_y
			new_value = cavern1[cavern_old_row_index][cavern_old_column_index] + column_adder + row_adder
			if new_value > 9:
				cavern_all[row_index][column_index] = new_value - 9
			else:
				cavern_all[row_index][column_index] = new_value
			

print(cavern_all)	



class Cavern:
	def __init__(self, arr):
		self.cavern = arr
		self.risk_arr = np.ones_like(self.cavern, dtype=int)  * math.inf
		self.risk_arr[0][0] = 0
		self.open_list = [(0,0)]
		self.max_x, self.max_y = self.cavern.shape

	def evaluate(self):
		list_of_offsets = [(-1,  0),
						   ( 1,  0),
						   ( 0, -1),
						   ( 0,  1)]
		for x, y in self.open_list:
			# print(x, y)
			self.risk_arr[0][0] = 0
			for offset_x, offset_y in list_of_offsets:
				new_y = y + offset_y
				new_x = x + offset_x
				if new_x >= 0 and new_y >= 0 and new_x < self.max_x and new_y < self.max_y:
					if self.risk_arr[new_y][new_x] > self.cavern[new_y][new_x] + self.risk_arr[y][x]:
						self.risk_arr[new_y][new_x] = self.cavern[new_y][new_x] + self.risk_arr[y][x]
						self.open_list += [(new_x, new_y)]

	def display_risk(self):
		print(self.risk_arr)
				


	def display(self):
		for row in self.cavern:
			temp_str = ""
			for element in row:
				temp_str += " {}".format(element)
			print(temp_str)




cavern = Cavern(cavern_all)
cavern.evaluate()
cavern.display_risk()
# cavern.display_risk()

#2893