#
# number.py - list comprehension
#

numbers = [1,2,3,4,5]
print("List: ",numbers)

def triple(num):
    return num*3

tripled = []
tripled = [triple(i) for i in numbers]
print("Loop triple: ", tripled)

instring = str(input("Enter a string:"))
numstring = []
numstring = [i for i in instring if i.isdigit()]
print("Numstring: ", numstring)

words = input("Enter words: ")
capitalized = []
#first_letter = [w[0] for w in words]
capitalized = [ w[0].upper() + w[1:] for w in words.split()]
print("Capitalized: ", capitalized)
