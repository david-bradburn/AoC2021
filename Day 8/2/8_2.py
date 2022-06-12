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

seg_7_data = temp_data_split
seg_7_vals = temp_vals_split

full_cnt = 0

class seg_7():

    def __init__(self, data, vals):
        self.seg7_dict = {}
        self.seg7_dict_inv = {}
        self.temp_arr_len_5 = []
        self.temp_arr_len_6 = []

        self.data = data
        self.vals = vals


    def are_all_elements_x_in_y(self, x, y):#
        cnt = 0
        count_max = len(x)
        for seg in x:
            if seg in y:
                cnt += 1
        
        if cnt == count_max:
            return True
        else:
            return False

    
    def number_check(self, x, y):#
        cnt = 0
        if len(x) != len(y):
            return False
        
        count_max = len(y)
        for seg in x:
            if seg in y:
                cnt += 1
        
        if cnt == count_max:
            return True
        else:
            return False


    def find_number(self, arr, no_to_find, no_to_compare):
        for i in arr:
            if self.are_all_elements_x_in_y(self.seg7_dict_inv[no_to_compare], i):
                self.seg7_dict[i] = no_to_find
                self.seg7_dict_inv[no_to_find] = i
                arr.remove(i)
                # print(arr)
                return arr

    def find_number2(self, arr, no_to_find, no_to_compare):
        for i in arr:
            if self.are_all_elements_x_in_y(i, self.seg7_dict_inv[no_to_compare]):
                self.seg7_dict[i] = no_to_find
                self.seg7_dict_inv[no_to_find] = i
                arr.remove(i)
                # print(arr)
                return arr

    def __fill_seg7_dict(self):
        for i in self.data:
            match len(i):
                case(2):
                    self.seg7_dict[i] = 1
                    self.seg7_dict_inv[1] = i
                case(3):
                    self.seg7_dict[i] = 7
                    self.seg7_dict_inv[7] = i
                case(4):
                    self.seg7_dict[i] = 4
                    self.seg7_dict_inv[4] = i

                case(7):#length
                    self.seg7_dict[i] = 8
                    self.seg7_dict_inv[8] = i
                case(5):
                    self.temp_arr_len_5.append(i)
                case(6):
                    self.temp_arr_len_6.append(i)

        self.temp_arr_len_6 = self.find_number(self.temp_arr_len_6, 9, 4)
        self.temp_arr_len_6 =self.find_number(self.temp_arr_len_6, 0, 1)
        self.seg7_dict[self.temp_arr_len_6[0]] = 6
        self.seg7_dict_inv[6] = self.temp_arr_len_6[0]

        self.temp_arr_len_5 = self.find_number(self.temp_arr_len_5, 3, 7)
        self.temp_arr_len_5 = self.find_number2(self.temp_arr_len_5, 5, 6)
        # print(self.seg7_dict)
        self.seg7_dict[self.temp_arr_len_5[0]] = 2
        self.seg7_dict_inv[2] = self.temp_arr_len_5[0]  

        # print(self.seg7_dict)

        po = 3
        temp_no = 0
        # print(self.vals)
        for i in self.vals:
            for key in self.seg7_dict:
                # print(key, i)
                if self.number_check(key, i):
                    temp_no += 10**po * self.seg7_dict[key]
                    po -= 1
                    break

        return temp_no

    def main(self):
        return self.__fill_seg7_dict()

for p in range(len(seg_7_data)):
    dt = seg_7(seg_7_data[p], seg_7_vals[p])
    temp_cnt = dt.main()
    print(temp_cnt)
    full_cnt += temp_cnt
print(full_cnt)


## 1068933      


