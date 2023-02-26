#
# shelters.py - test animals.py
#

from animals import Dog, Cat, Bird, Shelter

print('\n#### Pet shelter program ####\n')

rspca = Shelter('RSPCA','Serpentine Meander', '12345')
rspca.newAnimal('Dog','Dude','1/1/2011','Brown','Jack Russell')
rspca.newAnimal('Dog','Brutus','1/1/1982','Brown','Rhodesian Ridgeback')
rspca.newAnimal('Cat','Oogie','1/1/2006','Grey','Fluffy')
rspca.newAnimal('Bird','Big Bird', '10/11/299','Yellow','Canary')
rspca.newAnimal('Bird','Dead Parrot','1/1/2011','Dead','Parrot')

print('\nAnimals added\n')

print('Listing animals for processing...\n')

rspca.displayProcessing()

#This code is commented out untill you have implemented
# the methods in animal.py 

print('Processing animals...\n')

rspca.makeAvailable('Dude')
rspca.makeAvailable('Oogie')
rspca.makeAvailable('Big Bird')
rspca.makeAvailable('Oogie')
rspca.makeAvailable('Tong Phuoc Trung Nguyen')

rspca.makeAdopted('Oogie')
rspca.makeAdopted('Big Bird')
rspca.makeAdopted('Oogie')

print('\nPrinting updated list...\n')

rspca.displayAll()
