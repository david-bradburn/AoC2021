
file = "input.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()
    input_stripped_split = []
    for i in input_raw:
        # print("egg")
        temp = i.strip("\n").split("|")[1]
        # print(temp.split(" "))
        temp_split = temp.split(" ")
        for i in temp_split:
            # print(i)
            if i == '':
                # print("Empty")
                pass
            else:
                input_stripped_split += [i]

clean_input = input_stripped_split

cnt = 0
for i in clean_input:
    match len(i):
        case (2 | 4 | 3 | 7): ## 1, 4, 7, 8
            cnt += 1

print(cnt)
# print(input_stripped_split)