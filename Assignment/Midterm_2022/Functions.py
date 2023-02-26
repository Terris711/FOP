#
# Functions.py - Question 3a
#

import numpy as np

# Create an array containing 10 values
Array = np.array([0,1,2,3,4,5,6,7,8,9])

# Create Sum function

def arraySum(Array):
    total = 0 
    for i in range(len(Array)):
        total += Array[i]
    return total


# Create Min function

def arrayMin(Array):
    min_value = Array[0]
    for i in range(len(Array)):
        min_value = min(min_value, Array[i])
    return min_value


# Create Max function

def arrayMax(Array):
    max_value = Array[0]
    for i in range(len(Array)):
        max_value = max(max_value, Array[i])
    return max_value


if __name__ == "__main__":

    Sum_of_array = arraySum(Array)
    print("Sum of the array = ", Sum_of_array)
    
    Min_of_array = arrayMin(Array)
    print("Min of the array = ", Min_of_array)

    Max_of_array = arrayMax(Array)
    print("Max of the array = ", Max_of_array)
