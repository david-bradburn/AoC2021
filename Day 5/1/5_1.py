import numpy as np

with open("../misc/test.txt", "r") as fd:
    input_raw = fd.readlines() ##.strip("\n").split("->")
    # for i in input_raw:
    input_striped = []
    input_cleaned_str = []
    temp = []
    for i in input_raw:
        input_striped += [i.strip('\n').split('->')]
    for index_1 in input_striped:
        temp = []
        for index_2 in index_1:
            # print(index_2)
            temp += [index_2.strip(' ').split(',')]
        input_cleaned_str += [temp]
    
    for i in range(len(input_cleaned_str)):
        for j in range(len(input_cleaned_str[i])):
            for k in range(len(input_cleaned_str[i][j])):
                input_cleaned_str[i][j][k] = int(input_cleaned_str[i][j][k])
    

print(input_cleaned_str)