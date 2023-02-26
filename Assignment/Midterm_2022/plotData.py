#
# plotData.py - Question 2c
#

import matplotlib.pyplot as plt

Names1 = ['part_1', 'part_2', 'part_3']
Values1 = [1, 10, 100]

plt.figure(figsize=(9, 3)) 

plt.subplot(131)
plt.bar(Names1, Values1)

plt.subplot(132)
plt.scatter(Names1, Values1)

plt.subplot(133)
plt.plot(Names1, Values1)
plt.suptitle('Different type of plotting')
plt.savefig('Display.png')

plt.show()
