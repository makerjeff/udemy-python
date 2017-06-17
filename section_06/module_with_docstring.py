"""
Use this to read a file. -JWX
"""

# read a file
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
