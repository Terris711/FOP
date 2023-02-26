#
# pops.py
#
pops = {'New South Wales': 7757843, 'Victoria' : 6100877,
        'Queensland' : 4860448,
        'South Australia' : 1710804,
        'Western Australia' : 2623164, 'Tasmania': 519783,
        'Northern Territory' : 245657, 'Australian Capital Territory': 398349}

print(pops['Victoria'])

total_pops = 0

for p in pops:
    print(p)

print()
print()

for k in pops.keys():
    print(k, ' : ', pops[k])
    total_pops += pops[k]
print("Total population: ",total_pops)

print()
print()
#The states and populations where the population is less than 3,000,000
print("States have population less than 3000.000")
for k in pops.keys():
    if pops[k] < 3000000:
        print(k, ' : ', pops[k])

print()

if "New Zealand" in pops.keys():
    print("New Zealand is a state")
else:
    print("New Zealand is not a state")