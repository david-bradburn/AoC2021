

import numpy as np

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

syn_dict_score = {")" : 3, 
                  "]" : 57,
                  "}" : 1197,
                  ">" : 25137}
corrupted_syn = []
for line in nav_syn:
    fifo = ""
    log = ""

    for bracket in line:
        log += bracket

        match bracket:
            case "(" | "[" | "{" | "<":
                fifo += bracket
            
            case ")" | "]" | "}" | ">":
                if fifo[-1] == syn_dict[bracket]:
                    # print(fifo)
                    fifo = fifo[:-1]
                else:
                    corrupted_syn += [bracket]
                    print("fifo ", fifo)
                    print("bracket", bracket)
                    print("log", log)
                    print("corrupted")
                    print("------------------------")
                    break

total = 0
for cor in corrupted_syn:
    total += syn_dict_score[cor]

print(total)

## 319233
