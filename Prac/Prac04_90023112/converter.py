#
# converter.py - convert between temperature format
#
from conversions import *

def uservalue(lower, upper, prompt):
    value = int(input())
    while value < lower or value > upper:
        print("Error - Please re-enter the number (", lower, "-", upper,")")
        value = int(input(prompt))
    return value

def main():
    again = True
    while again:
        print("Now, let's convert between our temperature format !")
        print("Conversion: \n 0 - fahr2cel\n 1 - cel2fahr\n 2 - cel2kel\n 3 - kel2cel\n 4 - fahr2kel\n 5 - kel2fahr")
        print("Please enter your choice of conversion between 0 and 5: ")
        conversion = uservalue(0,5,"Re-enter conversion: ")
        print(conversion)
        convertedvalue = float(input("Enter value to convert: "))
        if conversion == 0:
            answer = fahr2cel(convertedvalue)
        elif conversion == 1:
            answer = cel2fahr(convertedvalue)
        elif conversion == 2:
            answer = cel2kel(convertedvalue)
        elif conversion == 3:
            answer = kel2cel(convertedvalue)
        elif conversion == 4:
            answer = fahr2kel(convertedvalue)
        else:
            answer = kel2fahr(convertedvalue)
        print("Result is: ",answer)
        choice = input("Do you want to convert another one ? (Y/N)")
        if choice == "N":
            again = False
    print("Thank you so much <3 ")
if __name__ == "__main__":
    main()
