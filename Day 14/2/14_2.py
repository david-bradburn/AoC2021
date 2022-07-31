file = "input.txt"

DAY_NO = "14"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	starting_code = fd.readline().strip("\n")
	fd.readline()
	input_raw = fd.readlines()

	input_stripped = [comb.strip("\n").split(" -> ") for comb in input_raw]
	code_dict = {}
	for value in input_stripped:
		code_dict[value[0]] = value[1]


	code_ref_dict = {}
	for element_pair in code_dict:
		code_ref_dict[element_pair] = [element_pair[0] + code_dict[element_pair], code_dict[element_pair] + element_pair[1], code_dict[element_pair]]
	# print(input_stripped)

	# print(starting_code)
	# print(input_raw)

# print(code_ref_dict)

code = starting_code

## need to process the starting code:

code_pair_dict = {}
total_code_dict = {}
for index, element in enumerate(code):
	if element not in total_code_dict:
		total_code_dict[element] = 1
	else:
		total_code_dict[element] += 1

	try:
		element_pair_str = element + code[index + 1]
		if element_pair_str not in code_pair_dict:
			code_pair_dict[element_pair_str] = 1
		else:
			code_pair_dict[element_pair_str] += 1
	except IndexError:
		pass

print(code_pair_dict)
print(total_code_dict)	

no_of_steps = 40
for step in range(no_of_steps):
	new_code_pair_dict = {}
	for element_pair in code_pair_dict:
		first_new_code = code_ref_dict[element_pair][0]
		second_new_code = code_ref_dict[element_pair][1]
		new_code_element = code_ref_dict[element_pair][2]

		if first_new_code not in new_code_pair_dict:
			new_code_pair_dict[first_new_code] = code_pair_dict[element_pair]
		else:
			new_code_pair_dict[first_new_code] += code_pair_dict[element_pair]

		if second_new_code not in new_code_pair_dict:
			new_code_pair_dict[second_new_code] = code_pair_dict[element_pair]
		else:
			new_code_pair_dict[second_new_code] += code_pair_dict[element_pair]

		if new_code_element not in total_code_dict:
			total_code_dict[new_code_element] = code_pair_dict[element_pair]
		else:
			total_code_dict[new_code_element] += code_pair_dict[element_pair]


	code_pair_dict = new_code_pair_dict

print(code_pair_dict)
print(total_code_dict)	



max_total_key = max(total_code_dict, key=total_code_dict.get)
min_total_key = min(total_code_dict, key=total_code_dict.get)

	
print(total_code_dict[max_total_key] - total_code_dict[min_total_key])

#4110215602456
