import os
import sys
os.chdir(sys.path[0])


with open('name.txt') as file:
    read_file = file.read().split();
    print(f"First name is: {read_file[1]}")
    print(f"Middle name is: {read_file[2]}")
    print(f"Last Name is: {read_file[0]}")