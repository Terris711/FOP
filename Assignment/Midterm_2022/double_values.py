#
# double_values.py - Question 5c
#
import csv

with open ('doubled_values.csv','w') as output:
    doubled_values = csv.writer(output)
    fileobj = open('values.csv','r')
    data = fileobj.readlines()
    fileobj.close()

    doubled_numbers = []
    numbers = []

    for line in data:
        splitline = line.strip()
        numbers.append(int(splitline))

    doubled_numbers = [ n * 2 for n in numbers]

    doubled_values.writerow(doubled_numbers)

    
