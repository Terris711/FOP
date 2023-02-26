#
# extension.py - Throwing six-sided dice mutiple times
#

import random
dice = ['first','second','third','forth','fifth','sixth']
first = 0
second = 0
third = 0
forth = 0
fifth = 0 
sixth = 0
print('Please enter the number of throwing you want: ')
trials = int(input())

print('\nTHROWING DICE\n')

for index in range(trials):
    if random.choice(dice) == 'first' :
        first = first + 1
    if random.choice(dice) == 'second' :
        second = second + 1
    if random.choice(dice) == 'third' :
        third = third + 1
    if random.choice(dice) == 'forth' :
        forth = forth + 1
    if random.choice(dice) == 'fifth' :
        fifth = fifth + 1
    else:
        sixth = sixth + 1
print('\nThere were ', first, ' first & ', second, ' second & ', third, ' third & ', forth, ' forth & ', five, ' five & ', sixth.\n')

