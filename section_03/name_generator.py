import random
import string

final_string = ''

for i in range(0, 100):
    final_string += random.choice(string.ascii_letters)

print final_string