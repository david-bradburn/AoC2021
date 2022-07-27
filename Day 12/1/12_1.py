


file = "test1.txt"

DAY_NO = "12"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	# probably want to split the 
	input_raw = fd.readlines()
	input_stripped = []
	input_stripped += [i.strip("\n").split("-")for i in input_raw]

links = input_stripped


class Cave:

	def __init__(self, cave_name): #refactor and add cavetype
		 
		self.cave_name = cave_name
		if(self.cave_name == "start"):
			self.cave_type = "start"
		elif(self.cave_name == "end"):
			self.cave_type = "end"
		elif(self.cave_name.isupper()):
			self.cave_type = "large"
		elif(self.cave_name.islower()):
			self.cave_type = "small"
			self.visited = False
		else:
			raise Exception("Cave is not valid")
		

class CaveSystem:

	def create_network(self, map):
		for cave1, cave2 in map:
			cave1_typed = Cave(cave1)
			cave2_typed = Cave(cave2)

			if not (cave2_typed.cave_type == "start") and not (cave1_typed.cave_type == "end"):
				if (cave1 not in self.cave_network):
					self.cave_network[cave1] = [cave2_typed]
				else:
					self.cave_network[cave1] += [cave2_typed]

			if not (cave1_typed.cave_type == "start") and not (cave2_typed.cave_type == "end"):
				if cave2 not in self.cave_network:
					self.cave_network[cave2] = [cave1_typed]
				else:
					self.cave_network[cave2] += [cave1_typed]

	def display_cave_network(self):
		for key in self.cave_network:
			for cave in self.cave_network[key]:
				print(key, cave.cave_name, cave.cave_type)

	


	def __init__(self, map):
		self.cave_network = {}
		self.create_network(map)
		pass

caves = CaveSystem(links)

caves.display_cave_network()
