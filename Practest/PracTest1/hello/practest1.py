#
# practest1.py: print the letter that match the user's input
#

things = ['water','earth','fire','metal','fluffy bunnies']

for index in range(0,len(things)):
    print('Things : ', things[index])


choice = input('Please enter a letter...')
choice = choice.upper()

for item in things:
    if item.upper()[0] == choice:
        print('Your word: ', item)





