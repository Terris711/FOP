#
# people.py - object relationship between student and staff
#

class Address():

    def __init__(self,number, street, suburb, postcode):
        self.number = number
        self.street = street
        self.suburb = suburb
        self.postcode = postcode

    def __str__(self):
        return(self.number + ' ' + self.street + ' ' + self.suburb + ' ' + self.postcode)

class Person():

    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address

    def displayPerson(self):
        print('Name: ', self.name, '\tDOB: ', self.dob)
        print('         Address: ', self.address)

class Staff(Person):

    myclass = 'Staff'

    def __init__(self, name, dob, address, id):
        super().__init__(name, dob, address)
        self.id = id

    def displayPerson(self):
        super().displayPerson()
        print('         StaffID: ', self.id)

class Student(Person):

    myclass = 'Student'

    def __init__(self, name, dob, address, id):
        super().__init__(name, dob, address)
        self.id = id

    def displayPerson(self):
        super().displayPerson()
        print('         StudentID: ', self.id)

class Postgrad(Student):

    myclass = 'PostGraduate'

    def __init__(self, name, dob, address, id):
        super().__init__(name, dob, address, id)

    def displayPerson(self):
        super().displayPerson()
        print('         PostGraduateID: ', self.id)

class Undergrad(Student):

    myclass = 'UnderGraduate'

    def __init__(self, name, dob, address, id):
        super().__init__(name, dob, address, id)

    def displayPerson(self):
        super().displayPerson()
        print('         UnderGraduateID: ', self.id)
