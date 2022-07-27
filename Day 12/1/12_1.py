file = "test1.txt"

DAY_NO = "12"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	# probably want to split the 
	input_raw = fd.readlines()
	input_stripped = []
	input_stripped += [i.strip("\n").split("-")for i in input_raw]

print(input_stripped)


class cave:
	def __init__(self, cave_name): #refactor and add cavetype
		self.large_cave = False
		self.small_cave = False
		self.start_cave = False
		self.end_cave = False 
		self.cave_name = cave_name
		if(self.cave_name == "start"):
			self.start_cave = True
		elif(self.cave_name == "end"):
			self.end_cave = True
		elif(self.cave_name.isupper()):
			self.large_cave = True

print()