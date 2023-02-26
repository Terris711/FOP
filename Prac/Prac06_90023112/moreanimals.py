#
# moreanimals.py - read in animals from a file into a list of animal objects
#

from animals import Dog, Cat, Bird

myanimals = []

animalfile = open('animals.csv','r')
animaline = animalfile.readline()

while animaline:
    splitline = animaline.split(',')
    print(splitline)
    animaline = animalfile.readline()

    group = []
    if splitline[0] =='Dog':
        group = Dog(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    elif splitline[0] == 'Cat':
        group = Cat(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    elif splitline[0] == 'Bird':
        group = Bird(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    else:
        print('Unknown animal!', splitline[0])
    if group:
        myanimals.append(group)
    
animalfile.close()

for i in myanimals:
    i.printit()
    print()


