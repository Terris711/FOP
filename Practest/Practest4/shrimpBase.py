import random
import sys
import matplotlib.pyplot as plt
from shrimp import Shrimp

XMAX = 1000
YMAX = 500
    
def main(shrimpPop, graphOption):
    shrimpList = []
    numOfShrimp = 15

# a. The initial population of shrimp as an integer (default = 15)
    if shrimpPop:
        numOfShrimp = int(shrimpPop) 


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

        # Shrimp multiply at a rate of 8%
        for i in range(int(numOfShrimp * 0.08)):
            randX = random.randint(0, XMAX)
            randY = random.randint(0, YMAX)
            shrimpList.append(Shrimp([randX, randY], [XMAX, YMAX]))

        # b. A Y/N option as a string for showing the plots. “Y” shows the plot at each timestep and “N” doesn’t show the plot at all (default to “Y”) (1 mark)
        if (not graphOption) or graphOption.upper() == "Y":
            plt.scatter(xvalues, yvalues)   # Note plt origin is bottom left 
            plt.xlim(0,XMAX)
            plt.ylim(0,YMAX)
            plt.pause(1)
            plt.clf()

    if graphOption.upper() == 'N':
        plt.scatter(xvalues, yvalues)   # Note plt origin is bottom left 
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.savefig('test.png')

    # Add code to shrimpBase.py to print out the initial population and final population separated by a comma

    print(str(numOfShrimp) + "," +   str(len(shrimpList)))

    
if __name__ == "__main__":
    parameter1 = None
    parameter2 = None

    # Because len(sys.argv) is always >= 1

    # if this value >= 2 then the first parameter exists
    if len(sys.argv) >= 2:
        parameter1 = sys.argv[1]
    # if this value >= 3 the the second parameter exists
    if len(sys.argv) >= 3:
        parameter2 = sys.argv[2]

    main(parameter1, parameter2)
