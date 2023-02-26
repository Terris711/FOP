import sys
import random
import matplotlib.pyplot as plt
from shrimp import Shrimp

XMAX = 1000
YMAX = 500
    
def main(Population,ShowGraph):
	shrimpList = []
	numOfShrimp = 15

	if Population and int(Population):
		numOfShrimp = int(Population)

	for i in range(numOfShrimp):
		randX = random.randint(0, XMAX)
		randY = random.randint(0, YMAX)
		shrimpList.append(Shrimp([randX, randY], [XMAX, YMAX]))
     
	for i in range(15):
		xvalues = []
		yvalues = []
	
		for shrimp in shrimpList:
			shrimp.stepChange()
			xvalues.append(shrimp.pos[0])
			yvalues.append(shrimp.pos[1])

		for i in range(int(numOfShrimp * 0.08)):
			randX = random.randint(0, XMAX)
			randY = random.randint(0, YMAX)
			shrimpList.append(Shrimp([randX, randY], [XMAX, YMAX]))
        
		if (not ShowGraph) or (ShowGraph.lower() == "y"):
			plt.scatter(xvalues, yvalues)
			plt.xlim(0,XMAX)
			plt.ylim(0,YMAX)
			#plt.pause(1)
			plt.clf()

	print(str(numOfShrimp) + "," + str(len(shrimpList)))
    
if __name__ == "__main__":
	arg1 = None
	arg2 = None

	if len(sys.argv) >= 2:
		arg1 = sys.argv[1]
	if len(sys.argv) >= 3:
		arg2 = sys.argv[2]

        main(arg1, arg2)
