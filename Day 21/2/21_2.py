#################################################################
###### https://adventofcode.com/2021/day/21 #####################
#################################################################

from turtle import pos


file = "input.txt"

DAY_NO = "21"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readlines()
	player_1_start_raw = int(input_raw[0].strip('\n')[-1])
	player_2_start_raw = int(input_raw[1].strip('\n')[-1])


print("Player 1 start position: {} \nPlayer 2 start position: {}".format(player_1_start_raw, player_2_start_raw))

MAX_SCORE = 21

class Game_Scores():
	def __init__(self) -> None:
		self.p1_games_won = 0
		self.p2_games_won = 0

	
	def p1_won(self):
		self.p1_games_won += 1
	
	def p2_won(self):
		self.p2_games_won += 1

# class Dirac_Dice_Game()

# 	def __init__(self) -> None:
# 		self.

class Dirac_Board():

	def __init__(self, p1_st: int, p2_st: int, p1_cur_score = 0, p2_cur_score = 0) -> None:
		self.p1_position = p1_st
		self.p1_score = 0
		self.p2_position = p2_st
		self.p2_score = 0
		
		self.p1_cur_score = p1_cur_score

		self.p2_cur_score = p2_cur_score

		self.player_turn = 0

		self.multiverse_score_counter = Game_Scores()
		self.quantum_rolls = [3, 4, 5, 6, 7, 8, 9]

		self.play()
		
	
	
	
	def update_position(self, cur_pos, roll):
		assert cur_pos <= 10
		assert roll < 10

		new_pos = cur_pos + roll
		
		if new_pos > 10:
			new_pos -= 10

		return new_pos

	def roll_dice(self, position, score):
		new_universes = []
		for roll in self.quantum_rolls:
			temp = self.update_position(self, position, roll)
			new_universes += [temp, score + temp]

		return new_universes


		


	
	def play(self):


	

# 	def main(self):
# 		while (self.p1_score < MAX_SCORE) and (self.p2_score < MAX_SCORE):
# 			match self.player_turn:
# 				case 0:
# 					roll = self.roll_next_3_numbers()
# 					self.p1_position = self.update_position(self.p1_position, roll)
# 					self.p1_score += self.p1_position
# 					self.player_turn = 1
				
# 				case 1:
# 					roll = self.roll_next_3_numbers()
# 					self.p2_position = self.update_position(self.p2_position, roll)
# 					self.p2_score += self.p2_position
# 					self.player_turn = 0
		
# 		print(self.global_roll_counter)
# 		print(self.p1_score)
# 		print(self.p2_score)

			





# game = Dirac_Board(player_1_start_raw, player_2_start_raw)

##998088

