#
# zero.py - Question 4a - creating and resizing an array
#

import numpy as np

print("\nZERO ARRAY\n")
zeroarray = np.zeros((3,3,3))
print('Zero array size: ', np.size(zeroarray))
print('Zero arrayshape: ', np.shape(zeroarray), '\n') 
zeroarray [0][1][1] = 1
zeroarray [1][0][2] = 2
zeroarray [2][1][2] = 3
print(zeroarray)

zeroarray.resize((1,27))
print('\nZero array size: ', np.size(zeroarray))
print('Zero array shape: ', np.shape(zeroarray),'\n') 
print(zeroarray)

zeroarray.resize((3,9))
print('\nZero array size: ', np.size(zeroarray))
print('Zero array shape: ', np.shape(zeroarray),'\n') 
print(zeroarray)

