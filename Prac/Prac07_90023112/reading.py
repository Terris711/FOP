#
# reading.py - object relationship between student and staff
#

from people import *

listPeople = []
lines = None
while not lines:
    fname = input('Enter file name: ')
    try:
        with open('people.csv','r') as f:
            lines = f.readlines()
    except ValueError as err:
        print('Error with file open: ', err)
    except:
        print('Unexpected error: ', err)

for line in lines:
    temp = None
    splitline = line.strip().split(':')
    if splitline[0] == 'Staff':
        temp = Staff(splitline[1], splitline[2], splitline[3], splitline[4])
    elif splitline[0] == 'Postgrad':
        temp = Postgrad(splitline[1], splitline[2], splitline[3], splitline[4])
    elif splitline[0] == 'Undergrad':
        temp = Undergrad(splitline[1], splitline[2], splitline[3], splitline[4])
    if temp:
        listPeople.append(temp)

for i in listPeople:
    i.displayPerson()
