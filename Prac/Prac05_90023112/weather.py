#
# weather.py: Print min and max temps from a file 
# (source: http://www.bom.gov.au/climate/)

import matplotlib.pyplot as plt

fileobj = open('marchweather.csv', 'r') 

minsline = fileobj.readline()
maxsline = fileobj.readline()

fileobj.close()

minsplitline = minsline.strip().split(',') 
maxsplitline = maxsline.strip().split(',')
print(maxsplitline)
print(minsplitline)

mins = [float(i) for i in minsplitline]
maxs = [float(i) for i in maxsplitline]
dates = range(1,32)

plt.plot(dates, mins, dates, maxs) 
plt.show()
