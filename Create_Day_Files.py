
import os

def ask_for_day():
    day_no = str(input("Enter day no: "))
    return day_no

def make_part_folder_and_files(day_path_i, day, part):
    part_path = os.path.join(day_path_i, str(part))
    os.mkdir(part_path)
    day_python_file_name = str(day) + "_" + str(part) + ".py"
    file_path  = os.path.join(part_path, day_python_file_name)
    f = open(file_path, "w")
    boiler_plate_fd = open("day_boilerplate.txt", "r")

    boiler_plate_arr = boiler_plate_fd.readlines()
    boiler_plate_str = ""
    for line in boiler_plate_arr:
        boiler_plate_str += line
    boiler_plate = boiler_plate_str.format(day, part)
    
    f.write(boiler_plate)
    f.close()



def main():
    day_no = ask_for_day()
    day_str = "Day " + day_no
    current_wd = os.getcwd()
    try:
        day_path = os.path.join(current_wd, day_str)
        os.mkdir(day_path)
    except FileExistsError:
        print("Folder Day {} already exists".format(day_no))
        return

    make_part_folder_and_files(day_path, day_no, 1)
    make_part_folder_and_files(day_path, day_no, 2)

    misc_path = os.path.join(day_path, "misc")
    try:
        os.mkdir(misc_path)
    except FileExistsError:
        print("Misc file already exists")
        return





main() 