#################################################################
###### https://adventofcode.com/2021/day/21 #####################
#################################################################

# from turtle import pos


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

	
	def player_won(self, player, no_universes):
		match player:
			case 0:
				self.p1_games_won += no_universes
			case 1:
				self.p2_games_won += no_universes

		
	
	def p2_won(self, no_universes):
		self.p2_games_won += no_universes

# class Dirac_Dice_Game()

# 	def __init__(self) -> None:
# 		self.

class Dirac_Board():

	def __init__(self, p1_st: int, p2_st: int) -> None:

		self.player_pos_arr= [p1_st, p2_st]
		self.player_score_arr = [0, 0]

		self.MAX_SCORE = 21

		self.multiverse_score_counter = Game_Scores()
		self.quantum_rolls = [3, 4, 5, 6, 7, 8, 9]
		self.no_of_universes = [1, 3, 6, 7, 6, 3, 1]

		self.play()
		
	
	
	
	def update_position(self, cur_pos, roll):
		assert cur_pos <= 10
		assert roll < 10

		new_pos = cur_pos + roll
		
		if new_pos > 10:
			new_pos -= 10

		return new_pos



		

##Need to do a path finding style recursion of the universes. Times the number as you go,
	def player_takes_turn(self, player_turn, position_arr: list, score_arr: list, no_universes: int) -> None:
		temp_position_arr = [0, 0]
		temp_score_arr = [0, 0]
		temp_position_arr[not player_turn] = position_arr[not player_turn]
		temp_score_arr[not player_turn] = score_arr[not player_turn]

		for roll_index, roll in enumerate(self.quantum_rolls):
			temp_position_arr[player_turn] = self.update_position(position_arr[player_turn], roll)
			temp_score_arr[player_turn] = score_arr[player_turn] + temp_position_arr[player_turn]
			temp_no_universe = no_universes * self.no_of_universes[roll_index]

			if temp_score_arr[player_turn] >= self.MAX_SCORE:	
				self.multiverse_score_counter.player_won(player_turn, temp_no_universe)
				continue
			else:
				self.player_takes_turn(not player_turn, temp_position_arr, temp_score_arr, temp_no_universe)


	def play(self):
		player_turn = 0
		self.player_takes_turn(player_turn, self.player_pos_arr, self.player_score_arr, 1)
		print(self.multiverse_score_counter.p1_games_won)
		print(self.multiverse_score_counter.p2_games_won)
		print("--------------")
		

		

# game = Dirac_Board	


game = Dirac_Board(player_1_start_raw, player_2_start_raw)


## 306621346123766
