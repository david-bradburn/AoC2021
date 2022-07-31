


file = "test.txt"

DAY_NO = "14"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	starting_code = fd.readline().strip("\n")
	fd.readline()
	input_raw = fd.readlines()

	input_stripped = [comb.strip("\n").split(" -> ") for comb in input_raw]
	code_dict = {}
	for value in input_stripped:
		code_dict[value[0]] = value[1]
	# print(input_stripped)

	# print(starting_code)
	# print(input_raw)


code = starting_code

total_dict = {}
for i in code:
	if i not in total_dict:
		total_dict[i] = 0
print(code)
no_of_steps = 10
for step in range(no_of_steps):
	new_code = ""
	for index, element in enumerate(code):
		# print(element, index)
		new_code += element
		try:
			new_code += code_dict[element + code[index+1]]
		except IndexError:
			print("Step {} completed".format(step+1))
			# print("End of step")
			# print("New code {}".format(new_code))
			pass
	
	code = new_code


for element in code:
	if element in total_dict:
		total_dict[element] += 1
	else:
		total_dict[element] = 1

print(total_dict)
max_total_key = max(total_dict, key=total_dict.get)
min_total_key = min(total_dict, key=total_dict.get)

	
print(total_dict[max_total_key] - total_dict[min_total_key])