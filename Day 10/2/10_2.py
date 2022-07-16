

file = "input.txt"
file_path = "../misc/"
with open(file_path + file, "r") as fd:
    input_raw = fd.readlines()
    input_stripped = []
    input_stripped += [i.strip("\n") for i in input_raw]

nav_syn = input_stripped
# for line in nav_syn:
#     print(line)


syn_dict = {")" : "(", 
            "]" : "[",
            "}" : "{",
            ">" : "<"}

syn_dict_score = {"(" : 1, 
                  "[" : 2,
                  "{" : 3,
                  "<" : 4}

                
# corrupted_syn = []
corrupted_lines = []
all_fifo = []
# fifo
for indx, line in enumerate(nav_syn):
    fifo = ""
    # log = ""

    for bracket in line:
        # log += bracket

        match bracket:
            case "(" | "[" | "{" | "<":
                fifo += bracket
            
            case ")" | "]" | "}" | ">":
                if fifo[-1] == syn_dict[bracket]:
                    fifo = fifo[:-1]
                else:
                    # corrupted_syn += [bracket]
                    corrupted_lines += [indx]
                    break
                    
    all_fifo += [fifo]
    # print(fifo)

print(all_fifo)
print(corrupted_lines)

# print(all_fifo == corrupted_lines)
incomplete_lines_revresed = []
for indx, i in enumerate(all_fifo):
    if indx in corrupted_lines:
        pass
    else:
        incomplete_lines_revresed += [i[::-1]]

print(incomplete_lines_revresed)

list_of_totals = []

for index, line in enumerate(incomplete_lines_revresed):
    temp = 0
    for bracket in line:
        temp = temp * 5 + syn_dict_score[bracket]
    
    list_of_totals += [temp]

print(list_of_totals)

while(len(list_of_totals) > 1):
    list_of_totals.remove(max(list_of_totals))
    list_of_totals.remove(min(list_of_totals))

print(list_of_totals[0])

## 1118976874
