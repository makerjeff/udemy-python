"""
Use this to read a file.

How to use:
    - eat a peanut.
    - then eat a cherry.
    - then vomit it all back out.

Notes:
    - there are none.
"""

# read a file
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
