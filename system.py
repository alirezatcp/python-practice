import sys
import os

print(sys.path) # shows pathes we can use in this script. we can add another path with this command (TODO): sys.path.append(r'new_path_directory') 


print(__file__) # shows program address

print(__name__) # print program name

print(dir(sys)) # name of all funcs of sys library


print(os.getcwd()) # get this file directory path.

print(os.path.exists('./text_file')) # shows is this file exests or not

os.remove('./text_file') # remove given file


