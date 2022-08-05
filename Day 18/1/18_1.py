import ast


file = "test_explode.txt"

DAY_NO = "18"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readline()
	list_of_sn_nos = ast.literal_eval(input_raw) ## convert this is a coord esk class system.
	
	print(input_raw)
	print(list_of_sn_nos)


test_list = [[1, 2], [3, 4]]

print(list.index(test_list, 2))


# class SN_Numbers:

# 	def __init__(self, ):

