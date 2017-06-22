import random, string

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_letters

def generate(input1, input2, input3):

    if input1 == 'v':
        letter1 = random.choice(vowels)
    elif input1 == 'c':
        letter1 = random.choice(consonants)
    elif input1 == 'l':
        letter1 = random.choice(letter)
    else:
        letter1 = input1

    if input2 == 'v':
        letter2 = random.choice(vowels)
    elif input2 == 'c':
        letter2 = random.choice(consonants)
    elif input2 == 'l':
        letter2 = random.choice(letter)
    else:
        letter2 = input2

    if input3 == 'v':
        letter3 = random.choice(vowels)
    elif input3 == 'c':
        letter3 = random.choice(consonants)
    elif input3 == 'l':
        letter3 = random.choice(letter)
    else:
        letter3 = input3

    name = letter1+letter2+letter3
    return name


def Main():
    letter_input_1 = raw_input("What type of letter? Enter 'v' for vowel, 'c' for consonant, 'l' for any letter -> ")
    letter_input_2 = raw_input("What type of letter? Enter 'v' for vowel, 'c' for consonant, 'l' for any letter -> ")
    letter_input_3 = raw_input("What type of letter? Enter 'v' for vowel, 'c' for consonant, 'l' for any letter -> ")

    print 'Your random names: '

    for i in range(20):
        print generate(letter_input_1, letter_input_2, letter_input_3)


if __name__ == '__main__':
    Main()