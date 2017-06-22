import random, string

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_letters

letter_input_1 = raw_input("What type of letter? Enter 'v' for vowel, 'c' for consonants, 'l' for any letter -> ")
letter_input_2 = raw_input("What type of letter? Enter 'v' for vowel, 'c' for consonants, 'l' for any letter -> ")
letter_input_3 = raw_input("What type of letter? Enter 'v' for vowel, 'c' for consonants, 'l' for any letter -> ")

print letter_input_1, letter_input_2, letter_input_3

# verbose version
def generator():
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        letter1 = random.choice(letter)
    else:
        letter1 = letter_input_1

    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input_2

    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_input_3 == 'l':
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input_3

    return letter1 + letter2 + letter3

def Main():
    print "Your 3 letter string: " + generator()

if __name__ == '__main__':
    Main()