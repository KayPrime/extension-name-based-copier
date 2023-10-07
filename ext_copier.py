#! /usr/bin/python3

import os, shutil,sys

file_path = "."
ext_name = sys.argv[1]

file_ex = []

def get_file_extension():

    for files in os.listdir(file_path):
        index = files.rfind(".")+1
        if files[index:] not in file_ex:
            file_ex.append(files[index:])

def check_and_copy():
    if ext_name in file_ex:
        new_dir_path = os.path.join(file_path, ext_name)
        os.mkdir(new_dir_path)
        for files in os.listdir(file_path):
            if os.path.isfile(files):
                if files.endswith("." + ext_name):
                    source_path = os.path.join(file_path, files)
                    destination_path = os.path.join(new_dir_path, files)
                    shutil.copy(source_path, destination_path)
    else:
        return "there's no file with that extension in this directory"

def main():
    get_file_extension()
    check_and_copy()

main()
