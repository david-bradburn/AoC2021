import ast
from pickle import FALSE, TRUE

file = "test_explode.txt"

DAY_NO = "18"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readline()
	list_of_sn_nos = ast.literal_eval(input_raw) ## convert this is a coord esk class system.
	
	# print(input_raw)
	# print(list_of_sn_nos)



test_list = [[[1, 6], 2], [3, [4, 5]]]




# print(list.index(test_list, 2))


class SN_Numbers:

	def __init__(self, test_arr):

		self.sn_no = test_arr
		self.left = "0"
		self.right = "1"

		self.depth = 1
		
		self.index_str = ""
		self.sn_list = [] #depth, value


	def process_list(self, arr):
		for no in arr:

			if type(no) == list:
				if type(no[0]) == int and type(no[1]) == int:
					self.sn_list += [[self.depth + 1, no]]
				else:
					self.depth += 1
					self.process_list(no)
					self.depth -= 1

			elif type(no) == int:
				self.sn_list += [[self.depth, no]]
				


	def explode(self):
		DEPTH_INDEX = 0
		SN_NO_INDEX = 1

		LEFT_INDEX = 0
		RIGHT_INDEX = 1


		for index, value in enumerate(self.sn_list):
			if value[DEPTH_INDEX] > 4: # It's time to explode
				if index > 0:
					left_sn_index = index - 1
					

					self.sn_list[left_sn_index][SN_NO_INDEX] += value[SN_NO_INDEX][LEFT_INDEX]


				if index < len(self.sn_list):
					right_sn_index = index + 1
					self.sn_list[right_sn_index][SN_NO_INDEX] += value[SN_NO_INDEX][RIGHT_INDEX]

				self.sn_list[index][DEPTH_INDEX] -= 1
				self.sn_list[index][SN_NO_INDEX] = 0

				return TRUE
		return FALSE
	



	def display_sn_no(self):
		print(self.sn_list)

print(list_of_sn_nos)


test = SN_Numbers(list_of_sn_nos)
test.process_list(test.sn_no)
test.display_sn_no()
test.explode()
test.display_sn_no()

				

