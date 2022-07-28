


file = "input.txt"

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
		else:
			raise Exception("Cave is not valid")
		self.visited = False

class CaveSystem:

	def create_network(self, map):
		for cave1, cave2 in map:
			cave1_typed = Cave(cave1)
			cave2_typed = Cave(cave2)

			if not (cave2_typed.cave_type == "start") and not (cave1_typed.cave_type == "end"):
				if (cave1 not in self.cave_network):
					self.cave_network[cave1] = [cave2]
				else:
					self.cave_network[cave1] += [cave2]

			if not (cave1_typed.cave_type == "start") and not (cave2_typed.cave_type == "end"):
				if cave2 not in self.cave_network:
					self.cave_network[cave2] = [cave1]
				else:
					self.cave_network[cave2] += [cave1]

	def create_cave_list(self):
		for cave_key in self.cave_network:
			self.cave_list[cave_key] = Cave(cave_key)

		self.cave_list["end"] = Cave("end")


	def display_cave_network(self):
		for key in self.cave_network:
			for cave in self.cave_network[key]:
				# print(key, cave)
				print(key, cave, self.cave_list[cave].cave_type)
	

	def traverse(self, cave):
		local_cave_type = self.cave_list[cave].cave_type
		if local_cave_type == "end":
			self.no_of_valid_routes += 1
			self.list_of_routes += [self.path_through_cave_system]
			print(self.list_of_routes[-1])
			return 

		elif local_cave_type == "small":
			self.cave_list[cave].visited = True
		
		elif local_cave_type == "large":
			pass
		else:
			print("At start point")

		for cave_option in self.cave_network[cave]:
			if not self.cave_list[cave_option].visited:
				self.path_through_cave_system += [cave_option]
				self.traverse(cave_option)
				self.cave_list[cave_option].visited = False
				self.path_through_cave_system = self.path_through_cave_system[:-1]

		return 


	


	def __init__(self, map):
		self.cave_list = {}
		self.path_through_cave_system = ["start"]
		self.cave_network = {}
		self.list_of_routes = []
		self.no_of_valid_routes = 0
		self.create_network(map)
		self.create_cave_list()
		

caves = CaveSystem(links)

caves.display_cave_network()

caves.traverse("start")
print(caves.no_of_valid_routes)


# 4720
