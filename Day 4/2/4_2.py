# from cProfile import run
import numpy as np

with open("../misc/input.txt", "r") as fd:
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

print(input)
boards_proccesed_np = np.array(boards_proccesed, dtype=int)
# print(boards_proccesed_np)
board_check_array = np.zeros(boards_proccesed_np.shape, dtype=int)
# print(board_check_array)



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
        for j in range(x): #row...
            count = 0
            for k in range(y): #col
                if arr[i, j, k] == 1:
                    count += 1
            if count == 5:
                return True, i

    return False, -1

def check_col(arr):
    no_of_boards, x, y = arr.shape
    for i in range(no_of_boards):
        for k in range(y): #col
            count = 0
            for j in range(x): #row
                if arr[i, j, k] == 1:
                    count += 1
            if count == 5:
                return True, i

    return False, -1


def check_win(arr):
    win_1, board_index_1 = check_row(arr)
    if win_1:
        print("Winning board via row found")
        print(arr[board_index_1])
        return True, board_index_1
    
    win_2, board_index_2 = check_col(arr)
    if win_2:
        print("Winning board via column found")
        print(arr[board_index_2])
        return True, board_index_2

    return False, -1

    

winning_board_found = True
board_index = 0
iter_counter = 0

while len(boards_proccesed_np) != 1:
    print("Iteration {}".format(iter_counter))
    iter_counter += 1
    input_val = input.pop(0)
    print(input_val)
    tick_off_value(boards_proccesed_np, input_val)
    print(board_check_array)
    winning_board_found = True
    while winning_board_found:
        winning_board_found, board_index = check_win(board_check_array)
        if(winning_board_found):
            print("board \n{} \n to be deleted".format(boards_proccesed_np[board_index]))
            boards_proccesed_np = np.delete(boards_proccesed_np, board_index, 0)
            board_check_array = np.delete(board_check_array, board_index, 0)

winning_board_found = False
while not winning_board_found:
    print("Iteration {}".format(iter_counter))
    iter_counter += 1
    input_val = input.pop(0)
    print(input_val)
    tick_off_value(boards_proccesed_np, input_val)
    print(board_check_array)
    winning_board_found, board_index = check_win(board_check_array)


print(boards_proccesed_np[0])
print(board_check_array[0])

running_sum = 0
for x in range(5):
    for y in range(5):
        running_sum += ((not board_check_array[board_index, x, y]) * boards_proccesed_np[board_index, x, y])

print(running_sum)
print(input_val)
print(running_sum * input_val)

##4495