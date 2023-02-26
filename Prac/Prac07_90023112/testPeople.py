#
# testPeople.py - test people.py
#

from people import Address, Person, Staff, Student

print('### People Tesst Program ###')

testAdd = Address('10', 'Downing st', 'Carlisle', '6101')
testPerson = Person('Winston Churchill', '30/11/1874', testAdd)
testPerson.displayPerson()
print()

testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
testPerson2 = Staff('Professor Awesome', '1/6/191', testAdd2, '12345J')
testPerson2.displayPerson()
print()

testAdd3 = Address('7', 'Mauritius', 'Waikiki', '6169')
testPerson3 = Student('Thi Van Anh Duong', '20/05/2001', testAdd3, '90023112')
testPerson3.displayPerson()
print()

testAdd4 = Address('9', 'Mikiki', 'Los Angles', '9090')
testPerson4 = Student('Trung Nguyen Tong Phuoc', '17/08/2001', testAdd4, '90023112')
testPerson4.displayPerson()
print()

testAdd5 = Address('53', 'Be. Hotel', 'Freemantle', '6179')
testPerson5 = Student('Anna Duong', '19/05/2001', testAdd5, '90023112')
testPerson5.displayPerson()
print()

