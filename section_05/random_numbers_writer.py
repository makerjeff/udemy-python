from random import *

def create_random_data(upper_limit):

    rand_array = []

    for item in range(upper_limit):
        rand_array.append(randint(0, 255))

    return rand_array


def Main():
    file = open('random_numbers.txt', 'w')

    for item in create_random_data(100):
        file.write(str(item) + '\n')

    file.close()



if __name__ == '__main__':
    Main()



