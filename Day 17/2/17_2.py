import math


file = "input.txt"

DAY_NO = "17"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	input_raw = fd.readline().strip("\n").split("..")
	input_split1 = []
	for i in input_raw:
		input_split1 += i.split("=")

	input_split2 = []
	for i in input_split1:
		input_split2 += i.split(",")

	match input_split2:
		case ["target area: x", x1, x2, " y", y2, y1]:
			target = [int(x1), int(x2), int(y1), int(y2)]
		case _:
			raise Exception


class Cravas:

	def __init__(self, target: list) -> None:
		self.vx = 0
		self.vy = 0
		self.px = 0
		self.py = 0
		self.max_y = 0
		self.no_of_steps = 0

		self.n_contine_steps = 0

		self.pt_x1 = int(target[0])
		self.pt_x2 = int(target[1])
		self.pt_y1 = int(target[2])
		self.pt_y2 = int(target[3])

		self.possible_starting_velocities = {}


	def reset_shot(self, vx, vy):
		self.init_vx = vx
		self.init_vy = vy
		self.vx = vx
		self.vy = vy
		self.px = 0
		self.py = 0
		self.max_y = 0
		self.n_contine_steps = 0
		self.no_of_steps = 0
	

	def update_max_y(self):
		if(self.py > self.max_y):
			self.max_y = self.py
	

	def check_probe_location(self):
		in_target = (self.px <= self.pt_x2) and (self.px >= self.pt_x1) and (self.py <= self.pt_y1) and (self.py >= self.pt_y2)
		past_target = (self.px > self.pt_x2) or (self.py < self.pt_y2)

		if in_target:
			self.possible_starting_velocities[(self.init_vx, self.init_vy)] = self.max_y
			return True
		elif past_target:
			return True
		else:
			return False
	

	def shoot_probe(self):
		while not self.n_contine_steps:
			# print(self.px, self.py)
			self.px += self.vx
			self.py += self.vy

			if self.vx > 0:
				self.vx -= 1
			# elif self.vx < 0:
			# 	self.vx += 1

			self.vy -= 1
			# self.no_of_steps += 1
			self.update_max_y()

			self.n_contine_steps = self.check_probe_location()


	def scan_shots(self, lower_limit_vx, upper_limit_vx, lower_limit_vy, upper_limit_vy):

		for vx in range(lower_limit_vx, upper_limit_vx):
			for vy in range(lower_limit_vy, upper_limit_vy):
				# print(vx, vy)
				self.reset_shot(vx, vy)
				self.shoot_probe()

			print(vx)

	

		
		print(len(self.possible_starting_velocities))
		# max_total_key = max(self.possible_starting_velocities, key=self.possible_starting_velocities.get)
		# print("{}: {}".format(max_total_key, self.possible_starting_velocities[max_total_key]))




x = Cravas(target)
n = 0.5 + math.sqrt(2*(target[0] - 1) + 0.25)
n_floor = math.floor(n)
# n_ceiling = math.ceil(n)
# print(n_floor, n_ceiling)


x.scan_shots(n_floor, target[1] + 1, target[3], 3000)

#3767