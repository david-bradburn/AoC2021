import numpy as np

with open("../misc/test.txt", "r") as fd:
    input = list(map(int,fd.readline().strip("\n").split(","))) ## turns inputs into an array of ints
    boards = fd.readlines()

boards = [x.strip("\n") for x in boards][1:]
# print(boards)
# print("____")
boards = boards + [""]
# print(boards)
boards_proccesed = []
temp = []

cnt = 0

for x in boards:
    # print(x)
    if x == "":
        cnt += 1
        boards_proccesed += [temp]
        # print(temp)
        temp = []
    else:
        temp += [[int(i) for i in x.split(" ") if i]]

# print( )
# for i in range(cnt):
#     print(boards_proccesed[i])


boards_proccesed_np = np.array(boards_proccesed, dtype=int)
print(boards_proccesed_np)
board_check_array = np.zeros(boards_proccesed_np.shape, dtype=int)
print(board_check_array)



def tick_off_value(arr, val):
    no_of_boards, x, y = arr.shape
    # print(no_of_boards, x, y)
    for i in range(no_of_boards):
        for j in range(x):
            for k in range(y):
                if arr[i,j,k] == val:
                    board_check_array[i,j,k] = 1

def check_row(arr):
    no_of_boards, x, y = arr.shape
    for i in range(no_of_boards):
        for j in range(x): #row
            count = 0
            for k in range(y): #col
                if arr[i, j, k] == 1:
                    count += 1
            if count == 5:
                return True, i, j ,k

    return False, -1, -1, -1

def check_col(arr):
    no_of_boards, x, y = arr.shape
    for i in range(no_of_boards):
        for k in range(y): #col
            count = 0
            for j in range(x): #row
                if arr[i, j, k] == 1:
                    count += 1
            if count == 5:
                return True, i, j ,k

    return False, -1, -1, -1


def check_win(arr):
    win, board, row, col = 

tick_off_value(boards_proccesed_np, 7)
print(board_check_array)
