#
# darts.py - Method of Darts for calculating Pi
#

import random
num_trials = 100000000

ncirc = 0
r = 1.0         #radius of circle
r2 = r*r

for i in range(num_trials):
    x = random.random()
    y = random.random()
    if ((x*x + y*y) <= r2):
        ncirc += 1

pi = 4.0 * ncirc / num_trials

print("\nFor ", num_trials, " trials, pi= ", pi)


#   The more I try the more different pi is, but it is not precise :<<
#   When I add more 0, it pretty precise
#   When I add more and more 0, it takes longer time to calculate 
