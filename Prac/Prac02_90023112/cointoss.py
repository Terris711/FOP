#
# cointoss.py - simulate tossing a coin multiplee times
#

import random

coin = ['heads','tails']
heads = 0
tails = 0
print('Please enter the number of tosses you want: ')
trials = int(input())

print('\nCOIN TOSS\n')

for index in range(trials):
    if random.choice(coin) == 'heads' :
        heads = heads + 1
    else:
        tails = tails + 1
print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')

