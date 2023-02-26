#
# Fibonacci.py - Question 1a
#

# Program to display the Fibonacci series up to nth term
num = int(input("How many terms? "))

# first two terms 
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid 
if num <= 0:
    print("Please enter a positive integer") 
elif num == 1:
    print("Fibonacci sequence up to" ,num,":") 
    print(n1)
else:
    print("Fibonacci sequence:") 
    while count < num:
        print(n1)
        nth = n1 + n2

# update values 
        n1 = n2
        n2 = nth 
    # count += 1 uses to increase the count value by 1 and control the while loop. While loop uses "count" value to check the condition in order to know whether or not it should continue (the while loop will stop when "count" value does not satisfy the condition. If we do not assign value for count variable, we can not check the condition to continue the while loop, it will run forever. 
        count += 1

