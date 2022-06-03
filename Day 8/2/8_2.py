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
    input_stripped_split = []
    for i in input_raw:
        # print("egg")
        temp_data = i.strip("\n").split("|")[0]
        temp_vals = i.strip("\n").split("|")[0]
        # print(temp.split(" "))
        temp_data_split = temp_data.split(" ")
        temp_vals_split = temp_vals.split(" ")

        for i in temp_vals_split:
            # print(i)
            if i == '':
                # print("Empty")
                pass
            else:
                input_stripped_split += [i]

### need to fix the file parsing
seg_7 = input_stripped_split
print(seg_7)
seg_7_dict_master = {"a": '', "b": '', "c": ' ', "d": '', "e": '', "f": '', "g": ''}




