#
# multilineplot.py - Question 2d
#

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2) 
t2 = t**2 
t3= t**3 
t4 = t**4

plt.figure(figsize = (9,3))

# plot t and t3 as red dots
plt.subplot(221)
plt.plot(t,t3,'ro')

# plot t2 and t4 as green dotted lines
plt.subplot(222)
plt.plot(t2,t4,'g:')
# add a supertitle "Four Powerful Plots" 
plt.suptitle("Four Powerful Plot")

# plot the four plots as subplots in a 2x2 grid 
# Create two more plots

plt.subplot(223)
plt.plot(t,t4, 'm|')

plt.subplot(224)
plt.plot(t3,t4, 'y2')

plt.show()
