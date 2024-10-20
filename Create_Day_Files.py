
import os
# from url import get_aoc_url

year = 2021

langtoext = {"python" : ["py", "bp_py.txt"] , "c++" : ["cpp", "bp_cpp.txt"]}


def ask_for_day():
    day_no = str(input("Enter day no: "))
    return day_no

def ask_for_language():
    ACCEPT_LANGUAGES = ["python", "c++"]
    msg_str = "Enter language : \n"
    for lang in ACCEPT_LANGUAGES:
        msg_str += f"  {lang}\n"
    lang = str(input(msg_str))
    try:
        assert (lang in ACCEPT_LANGUAGES)
        return lang
    except:
        print("Please enter a valid language")
        return ask_for_language()

def make_files(lang, filepath, day, part):
    day_file_name = str(day) + "_" + str(part) + f".{langtoext[lang][0]}"
    file_path  = os.path.join(filepath, day_file_name)
    print(day_file_name)
    f = open(file_path, "w")
    boiler_plate_fd = open(langtoext[lang][1], "r")

    boiler_plate_arr = boiler_plate_fd.readlines()
    boiler_plate_str = ""
    for line in boiler_plate_arr:
        boiler_plate_str += line

    boiler_plate = boiler_plate_str.format(year=year, day=day, part= part)
    print(boiler_plate)
    
    f.write(boiler_plate)
    f.close()

def make_part_folder_and_files(day_path_i, day, part, lang):
    part_path = os.path.join(day_path_i, str(part))
    try:
        os.mkdir(part_path)
    except FileExistsError:
        pass

    make_files(lang, part_path, day, part )
   


def main():
    day_no = ask_for_day()
    day_str = "Day " + day_no

    lang = ask_for_language()
    current_wd = os.getcwd()
    try:
        day_path = os.path.join(current_wd, day_str)
        os.mkdir(day_path)
    except FileExistsError:
        print("Folder Day {} already exists".format(day_no))
        part_path = os.path.join(day_path, str(1))
        day_file_name = str(day_no) + "_" + str(1) + f".{langtoext[lang][0]}"
        file_path  = os.path.join(part_path, day_file_name)

        if os.path.isfile(file_path):
            raise Exception(f"{file_path} already exists")


    make_part_folder_and_files(day_path, day_no, 1, lang)
    make_part_folder_and_files(day_path, day_no, 2, lang)

    misc_path = os.path.join(day_path, "misc")
    try:
        os.mkdir(misc_path)
    except FileExistsError:
        print("Misc file already exists")
        return

    # Creates test and input .txt for the day
    test_path = os.path.join(misc_path, "test.txt")
    input_path = os.path.join(misc_path, "input.txt")
     
    f = open(test_path, "w")
    f.close()
    f = open(input_path, "w")
    f.close()



main() 