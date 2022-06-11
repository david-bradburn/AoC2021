#
#    0:      1:      2:      3:      4:
#     aaaa    ....    aaaa    aaaa    ....
#    b    c  .    c  .    c  .    c  b    c
#    b    c  .    c  .    c  .    c  b    c
#     ....    ....    dddd    dddd    dddd
#    e    f  .    f  e    .  .    f  .    f
#    e    f  .    f  e    .  .    f  .    f
#     gggg    ....    gggg    gggg    ....
# 
#      5:      6:      7:      8:      9:
#     aaaa    aaaa    aaaa    aaaa    aaaa
#    b    .  b    .  .    c  b    c  b    c
#    b    .  b    .  .    c  b    c  b    c
#     dddd    dddd    ....    dddd    dddd
#    .    f  e    f  .    f  e    f  .    f
#    .    f  e    f  .    f  e    f  .    f
#     gggg    gggg    ....    gggg    gggg
#   

file = "input.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()
    temp_data_split = []
    temp_vals_split = []

    for i in input_raw:
        temp_data = i.strip("\n").split("|")[0]
        temp_vals = i.strip("\n").split("|")[1]

        temp_data_split += [temp_data.strip(" ").split(" ")]
        temp_vals_split += [temp_vals.strip(" ").split(" ")]
        
### need to fix the file parsing
print(temp_data_split)
print(temp_vals_split)

seg_7_data = temp_data_split
seg_7_vals = temp_vals_split
# print(seg_7)
seg_7_dict_master = {"a": '', "b": '', "c": '', "d": '', "e": '', "f": '', "g": ''}

class seg_7():
    def __init__(self, data, vals):
        self.a = ''
        self.b = ''
        self.c = ''
        self.d = ''
        self.e = ''
        self.f = ''
        self.g = ''
        self.data = data
        self.vals = vals
    
    
    def find_one_seg(self):
        


