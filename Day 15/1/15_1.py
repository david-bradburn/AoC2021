import numpy as np
from time import time


file = "input.txt"

DAY_NO = "15"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readlines()
	input_stripped = [line.strip("\n") for line in input_raw]
	max_x = len(input_stripped[0])
	max_y = len(input_stripped)
	assert max_x == max_y
	cavern1 = np.zeros((max_x, max_y), dtype=int)	
	for row_index, row in enumerate(input_stripped):
		for value_index, value in enumerate(row):
			cavern1[row_index][value_index] = value
			pass
	



class Cavern:
	def __init__(self, arr):
		self.cavern = arr
		self.risk_arr = np.ones_like(self.cavern, dtype=int) * 1000
		self.open_list = [(0,0)]

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
				if new_x >= 0 and new_y >= 0 and new_x < max_x and new_y< max_y:
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


N = 1
total_time = 0
for i in range(N):
	cavern = Cavern(cavern1)
	
	time1 = time()
	cavern.evaluate()
	time2 = time()
	total_time += time2- time1
print(total_time/N)
cavern.display_risk()
## 673