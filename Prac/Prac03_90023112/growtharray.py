#
# growtharray.py - simulation of unconstrained growth using array
#
import matplotlib.pyplot as plt
import numpy as np

print("\nSIMULATION - Uconstrained Growth\n")

length = 100
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = int(length / time_step)
growth_step = growth_rate * time_step

print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (sim length * time step per hour): ", num_iter)
print("Growth step (growth rate per time step): ", growth_step)

print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)

timesarray = np.zeros(num_iter + 1)
popsarray = np.zeros(num_iter + 1)

timesarray[0] = 0
popsarray[0] = population


for i in range(1, int(num_iter) + 1):

    growth = growth_step * population
    population = population + growth
    time = i * time_step
    timesarray[i] = time
    popsarray[i] = population
    print("Time: ", time, " \tGrowth: ", growth, " \tPopulation: ", population)

print("\nPROCESSING COMPLETE.\n")

plt.title('Prac 3.1: :Unconstrained Growth')
plt.plot(timesarray, popsarray, 'b--')
plt.show()



