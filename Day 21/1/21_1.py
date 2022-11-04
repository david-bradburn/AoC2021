#################################################################
###### https://adventofcode.com/2021/day/21 #####################
#################################################################

file = "input.txt"

DAY_NO = "21"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readlines()
	player_1_start_raw = input_raw[0].strip('\n')[-1]
	player_2_start_raw = input_raw[1].strip('\n')[-1]


print("Player 1 start position: {} \nPlayer 2 start position: {}".format(player_1_start_raw, player_2_start_raw))

class Dirac_Board():

	def __init__(self, p1_st, p2_st) -> None:
		self.p1_position = int(p1_st)
		self.p1_score = 0
		self.p2_position = int(p2_st)
		self.p2_score = 0
		self.seed = 1
		self.global_roll_counter = 0
		self.player_turn = 0
		self.global_roll_seed = 1
		# self.roll_next_3_numbers()
		self.main()
		

	def roll_next_3_numbers(self):
		assert self.global_roll_seed <= 100
		temp = 0
		for dice_value in range(self.global_roll_seed, self.global_roll_seed + 3):
			if dice_value > 100:
				temp += (dice_value - 100)
			else:
				temp += dice_value
		new_seed = self.global_roll_seed + 3
		if new_seed > 100:
			new_seed -= 100

		# print(temp, new_seed)
		self.global_roll_counter += 3
		self.global_roll_seed = new_seed
		return temp % 10

	def update_position(self, cur_pos, roll):
		assert cur_pos <= 10
		assert roll < 10

		new_pos = cur_pos + roll
		
		if new_pos > 10:
			new_pos -= 10

		return new_pos
	

	def main(self):
		while (self.p1_score < 1000) and (self.p2_score < 1000):
			match self.player_turn:
				case 0:
					roll = self.roll_next_3_numbers()
					self.p1_position = self.update_position(self.p1_position, roll)
					self.p1_score += self.p1_position
					self.player_turn = 1
				
				case 1:
					roll = self.roll_next_3_numbers()
					self.p2_position = self.update_position(self.p2_position, roll)
					self.p2_score += self.p2_position
					self.player_turn = 0
		
		print(self.global_roll_counter)
		print(self.p1_score)
		print(self.p2_score)

			





game = Dirac_Board(player_1_start_raw, player_2_start_raw)

##998088

