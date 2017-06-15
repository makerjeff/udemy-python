# ask user to input bill amount
# ask user to select a fixed percentage tip 15%, 18%, or 20%
# display tip amount and quit.

import os

os.system('clear')


def calculate_tip(bill_amount, tip_index):
    options = {0: 1.15, 1: 1.18, 2: 1.20}

    if int(tip_index) > 2:
        return 'Tip index out of range. '
    else:
        return float(bill_amount) * options[tip_index]



# print '{0:.2f}, {1:.1f}'.format(calculate_tip(45.44, 0), 100.111)


bill_amount = raw_input('bill amount? (:Q to quit) -> ')

while bill_amount != ':Q':
    tip_index = input('tip amount? 0.) 15%, 1.) 18%, 2.) 20% -> ')

    os.system('clear')

    print 'Your bill comes out to: {0:.2f}'.format(calculate_tip(bill_amount, tip_index))

    bill_amount = input('bill amount? (:Q to quit) -> ')