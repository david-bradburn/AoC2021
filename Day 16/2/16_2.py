#8 is new test
#9 is old test


# test_no = "8"
# file = "test{}.txt".format(test_no)

file = "input.txt"

DAY_NO = "16"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readlines()
	# assert len(inputraw) == 1
	bits_hex = [i.strip("\n") for i in input_raw]
	bits_bin = []
	for i in bits_hex:
		length_of_transmission = len(i) * 4
		bits_bin += [bin(int(i, 16))[2:].zfill(length_of_transmission)]
# print(bits_bin)

class BITS:

	def __init__(self, data: str) -> None:
		self.top_data_packet = data
		self.version_total = 0
		self.process_packet(0)

	def display_version_total(self):
		print("Version total: {}".format(self.version_total))

	def determine_length_type_id(self, version, type_id, packet_start_index, total_packet_length):
		# print(version)
		# print(type_id)
		length_type_id_index = packet_start_index + 6
		length_type_id = self.top_data_packet[length_type_id_index]
		# print(length_type_id)

		total_packet_length += 1

		match length_type_id:
			case "0":

				total_packet_length += 15

				sub_packet_length_processed_total = 0
				total_length_of_sub_packets_starting_index = length_type_id_index + 1
				total_length_of_sub_packets_end_index = total_length_of_sub_packets_starting_index + 15
				# print(total_length_of_sub_packets_starting_index)
				# print(total_length_of_sub_packets_end_index)
				total_length_of_sub_packets_bits = self.top_data_packet[total_length_of_sub_packets_starting_index: total_length_of_sub_packets_end_index]
				total_length_of_sub_packets_int = int(total_length_of_sub_packets_bits, 2)
				# print(total_length_of_sub_packets)

				print("Version: 0b{} \nType ID: 0b{}\nLength of sub packets: 0b{} ({})".format(version, type_id, total_length_of_sub_packets_bits, total_length_of_sub_packets_int))

				index_of_sub_packet = total_length_of_sub_packets_end_index
				literal_arr = []
				while sub_packet_length_processed_total < total_length_of_sub_packets_int:
					temp_packet_length, temp_literal = self.process_packet(index_of_sub_packet)
					literal_arr += [temp_literal]
					sub_packet_length_processed_total += temp_packet_length
					index_of_sub_packet += temp_packet_length
					# print(temp_packet_length)
				# print(sub_packet_length, total_length_of_sub_packets_int)


				total_packet_length += sub_packet_length_processed_total


			case "1":
				total_packet_length += 11
				total_no_of_sub_packets_start_index = length_type_id_index + 1
				total_no_of_sub_packets_end_index = total_no_of_sub_packets_start_index + 11

				total_no_of_sub_packets_bits = self.top_data_packet[total_no_of_sub_packets_start_index: total_no_of_sub_packets_end_index]
				total_no_of_sub_packets_int = int(total_no_of_sub_packets_bits, 2)

				print("Version: 0b{} \nType ID: 0b{}\nNo of sub packets: 0b{} ({})".format(version, type_id, total_no_of_sub_packets_bits, total_no_of_sub_packets_int))
				
				sub_packet_length_processed_total = 0
				index_of_sub_packet = total_no_of_sub_packets_end_index

				literal_arr = []
				for i in range(total_no_of_sub_packets_int):
					temp_packet_length, temp_literal = self.process_packet(index_of_sub_packet)
					literal_arr += [temp_literal]
					sub_packet_length_processed_total += temp_packet_length
					index_of_sub_packet += temp_packet_length

				total_packet_length += sub_packet_length_processed_total

		return total_packet_length, literal_arr
	
	def process_packet(self, packet_start_index):
		version = self.top_data_packet[packet_start_index:packet_start_index + 3]
		type_id = self.top_data_packet[packet_start_index + 3:packet_start_index + 6]
		self.version_total += int(version, 2)
		total_packet_length = 6
		literal_arr = []
		# print(type_id)
		match type_id:

			case "100": # 4, the next data is a literal
				
				literal_data = ""
				literal_offset = 0
				no_of_5_bits = 0
				literal_value = 0
				while True:
					no_of_5_bits += 1
					literal_header = self.top_data_packet[packet_start_index + 6 + literal_offset]
					literal_data += self.top_data_packet[packet_start_index + 7 + literal_offset : packet_start_index + 7 + literal_offset + 4]

					# literal_arr += [int(literal_data, 2)]
					# print(literal_header)
					# print(literal_data)
					if literal_header == "0":
						break
					else:
						literal_offset += 5
				
				print("Version: 0b{} \nType ID: 0b{}\nLiteral: 0b{} ({})".format(version, type_id, literal_data, int(literal_data, 2)))

				literal_value = int(literal_data, 2)
				total_packet_length += no_of_5_bits * 5 ## this does not account for the 0 bits that might follow on??????
				return total_packet_length, literal_value

			case "000": ##sum
				print("Sum of:")
				total_packet_length, literal_arr = self.determine_length_type_id(version, type_id, packet_start_index, total_packet_length)
				
				temp_sum = 0
				for i in literal_arr:
					temp_sum += i
				
				print("The sum of {} is {}".format(literal_arr, temp_sum))
				return total_packet_length, temp_sum
				

			case "001": # product
				print("Product of:")
				total_packet_length, literal_arr = self.determine_length_type_id(version, type_id, packet_start_index, total_packet_length)

				temp_product = 1
				for i in literal_arr:
					temp_product *= i
				
				print("The product of {} is {}".format(literal_arr, temp_product))
				return total_packet_length, temp_product

				
			
			case "010": ## minimum
				print("Minimum of:")
				total_packet_length, literal_arr = self.determine_length_type_id(version, type_id, packet_start_index, total_packet_length)
				temp_min = min(literal_arr)
				print("The minimum of {} is {}".format(literal_arr, temp_min))
				return total_packet_length, temp_min
			
			case "011":
				print("Maximum of:")
				total_packet_length, literal_arr = self.determine_length_type_id(version, type_id, packet_start_index, total_packet_length)

				temp_max = max(literal_arr)
				print("The maximum of {} is {}".format(literal_arr, temp_max))
				return total_packet_length, temp_max
			
			case "101":
				print("Greater than:")
				total_packet_length, literal_arr = self.determine_length_type_id(version, type_id, packet_start_index, total_packet_length)
				assert len(literal_arr) == 2

				temp_gt = literal_arr[0] > literal_arr[1]
				if temp_gt:
					print("{} is greater than {}".format(literal_arr[0], literal_arr[1]))
				else:
					print("{} is not greater than {}".format(literal_arr[0], literal_arr[1]))
				
				return total_packet_length, temp_gt

			
			case "110":
				print("Less than:")
				total_packet_length, literal_arr = self.determine_length_type_id(version, type_id, packet_start_index, total_packet_length)

				assert len(literal_arr) == 2

				temp_lt = literal_arr[0] < literal_arr[1]
				if temp_lt:
					print("{} is less than {}".format(literal_arr[0], literal_arr[1]))
				else:
					print("{} is not less than {}".format(literal_arr[0], literal_arr[1]))
				
				return total_packet_length, temp_lt

			case "111":
				print("Equal to:")
				total_packet_length, literal_arr = self.determine_length_type_id(version, type_id, packet_start_index, total_packet_length)

				assert len(literal_arr) == 2

				temp_eq = literal_arr[0] == literal_arr[1]
				if temp_eq:
					print("{} is equal to {}".format(literal_arr[0], literal_arr[1]))
				else:
					print("{} is not equal to {}".format(literal_arr[0], literal_arr[1]))
				
				return total_packet_length, temp_eq
			
			case _:
				raise Exception("Invalid type_id")



		return total_packet_length, literal_arr

for i in bits_bin:
	print("----------------------")
	bits = BITS(i)
	# bits.display_version_total()

# # 3408662834145