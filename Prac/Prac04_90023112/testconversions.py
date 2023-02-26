#
# testConversions.py - tests the functions in conversions.py
#
from conversions import *
print("\nTESTING CONVERSIONS\n")

testF = 100
testC = fahr2cel(testF)
print("Fahrenheit is ", testF, "Celcius is ", testC)
print(fahr2cel.__doc__)
print()

testC = 32
testF = cel2farh(testC)
print("Celcius is ", testC, "Fahrenheit is ", testF)
print()


testC = 32
testK = cel2kel(testC)
print("Celcius is ", testC, "Kelvin is ", testK)
print()


testK = 300
testC = kel2cel(testK)
print("Kelvin is ", testK, "Celcius is ", testC)
print()


testF = 320
testK = fahr2kel(testF)
print("Fahrenheit is ", testF, "Kelvin is ", testK)
print()


testK = 300
testF = kel2farh(testK)
print("Kelvin is ", testK, "Fahrenheit is ", testF)
print()
