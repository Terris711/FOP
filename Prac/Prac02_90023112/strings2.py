#
# strings2.py: Read in a string and print it forward 
#              using a while loop, a for loop and while loop

instring = input('Enter a string...')
# *** add upper and duplicating code here
instring = instring.upper() #2. Convert the string to upper case
instring = instring*2       #3. Duplicate the string
# forward with a while loop

print('Forward string is : ', end= '')
index = 1
while index < len(instring)-2:
    print(instring[index], end='')
    index = index + 2
print()

# forward  with a range loop

print('Forward string is : ', end='')
for index in range(1,len(instring)-2, 2):
    print(instring[index], end='')
print()

# forward with slicing

print('Forward string is :', instring[1:-2:2])



    
