


# test_no = "7"
# file = "test{}.txt".format(test_no)

file = "input.txt"

DAY_NO = "16"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	inputraw = fd.readlines()
	assert len(inputraw) == 1
	bits_hex = inputraw[0]
	length_of_transmission = len(bits_hex) * 4
	bits_bin = bin(int(bits_hex, 16))[2:].zfill(length_of_transmission)


class BITS:

	def __init__(self, data: str) -> None:
		self.top_data_packet = data
		self.version_total = 0
		self.process_packet(0)

	def display_version_total(self):
		print("Version total: {}".format(self.version_total))

	
	def process_packet(self, packet_start_index)-> list:
		version = self.top_data_packet[packet_start_index:packet_start_index + 3]
		type_id = self.top_data_packet[packet_start_index + 3:packet_start_index + 6]
		self.version_total += int(version, 2)
		total_packet_length = 6
		# print(type_id)
		match type_id:

			case "100": # 4, the next data is a literal
				
				literal_data = ""
				literal_offset = 0
				no_of_5_bits = 0
				while True:
					no_of_5_bits += 1
					literal_header = self.top_data_packet[packet_start_index + 6 + literal_offset]
					literal_data += self.top_data_packet[packet_start_index + 7 + literal_offset : packet_start_index + 7 + literal_offset + 4]

					# print(literal_header)
					# print(literal_data)
					if literal_header == "0":
						break
					else:
						literal_offset += 5
				
				print("Version: 0b{} \nType ID: 0b{}\nLiteral: 0b{} ({})".format(version, type_id, literal_data, int(literal_data, 2)))


				total_packet_length += no_of_5_bits * 5 ## this does not account for the 0 bits that might follow on??????



			
			case _:
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
						while sub_packet_length_processed_total < total_length_of_sub_packets_int:
							temp_packet_length = self.process_packet(index_of_sub_packet)
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
						for i in range(total_no_of_sub_packets_int):
							temp_packet_length = self.process_packet(index_of_sub_packet)
							sub_packet_length_processed_total += temp_packet_length
							index_of_sub_packet += temp_packet_length

						total_packet_length += sub_packet_length_processed_total



		return total_packet_length

bits = BITS(bits_bin)
bits.display_version_total()

# 999