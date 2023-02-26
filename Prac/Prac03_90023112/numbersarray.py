#
# numbersarray.py: Read in ten numbers and give sum, min, max and mean
#              
import numpy as np
import matplotlib.pyplot as plt

numarray = np.zeros(10)         #creates an empty array 10 elements long

print(' Enter ten numbers...')

for i in range(len(numarray)):
    print('Enter a number (', i, ')...')
    numarray[i] = int(input())
  
print('Total is', numarray.sum())

print('Min is', numarray.min())

print('Max is', numarray.max())

print('Mean is', numarray.mean())

plt.title('Array of numbers')
plt.plot(numarray,'c2')
plt.show()
