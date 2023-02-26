#
# animalis.py - object relationship between animals and shelters
#

class Animal():

    myclass = "Animal"

    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed

    def __str__(self):
        return(self.name + '|' + self.dob + '|' + self.colour + '|' + self.breed)

    def printit(self):
        spacing = 5 - len(self.myclass)
        print(self.myclass.upper(), spacing*' ' + ':',
              self.name,'\tDOB: ', self.dob,'\tColour: ',
              self.colour,'\tBreed: ', self.breed)

class Dog(Animal):
    myclass = "Dog"

class Cat(Animal):
    myclass = "Cat"

class Bird(Animal):
    myclass = "Bird"

class Shelter():

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.processing = []
        self.available = []
        self.adopted = []

    def displayProcessing(self):
        print('Current processing list:')
        for a in self.processing:
            a.printit()
            

    def displayAvailable(self):
        print('Current available list:')
        for a in self.available:
            a.printit()


    def displayAdopted(self):
        print('Current adopted list:')
        for a in self.adopted:
            a.printit()


    def displayAll(self):
        self.displayProcessing()
        self.displayAvailable()
        self.displayAdopted()

    def newAnimal(self, atype, name, dob, colour, breed):
        temp = None
        if atype == 'Dog':
            temp = Dog(name, dob, colour, breed)
        elif atype == 'Cat':
            temp = Cat(name, dob, colour, breed)
        elif atype == 'Bird':
            temp = Bird(name, dob, colour, breed)
        else:
            print('Error, unknown animal type: ', atype)

        if temp:
            self.processing.append(temp)
            print('Added ', name, ' to processing list')
            self.displayAll()

    def makeAvailable(self, name):
        temp = None
        position = 0 
        while not temp and position < len(self.processing):
            if self.processing[position].name == name:
                temp = self.processing[position]
            position += 1
        if temp:
            self.processing.remove(temp)
            self.available.append(temp)
            print(name,'is moved from processing to  available')
        else:
            print('Animal is not found')
                
            
    def makeAdopted(self, name):
        temp = None
        position = 0 
        while not temp and position < len(self.available):
            if self.available[position].name == name:
                temp = self.available[position]
            position += 1
        if temp:
            self.available.remove(temp)
            self.adopted.append(temp)
            print(name,'is moved from available  to  adopted')
        else:
            print('Animal is not found')
                


