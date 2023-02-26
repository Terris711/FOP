#
# plotter.py - read csv file
#
import matplotlib.pyplot as plt


def readfile(file_open):
    fileobj = open(file_open,'r')
    realines = fileobj.readlines()
    fileobj.close()
    return realines

def reading(xyvalues):
    values = xyvalues.strip().split(',')
    xyprint = [int(i) for i in values[1:]]
    return xyprint

def plotscatter(x,y,title,xlabel,ylabel):
    plt.scatter(x,y, color ='green')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plotline(x,y,title,xlabel,ylabel):
    plt.plot(x,y,'g--')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

dataline = readfile('data.csv')
xlabel = dataline[0]
ylabel = dataline[1]
x = reading(xlabel)
y = reading(ylabel)

print('X values: ',x)
print('Y values: ',y)
plotscatter(x,y,'Data Scatter','x label','y label')
plotline(x,y,'Data plotline','x label','y label')


