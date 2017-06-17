import os
import PIL as Image
import pickle
import sqlite3

# print this project's info
print __file__
print __name__
print os.path.realpath(__file__)

imported_modules = [os, Image, pickle, sqlite3]

def print_module_stats(module_list):

    for item in module_list:
        print item.__name__
        print item.__file__

def Main():
    print_module_stats(imported_modules)

if __name__ == '__main__':
    Main()