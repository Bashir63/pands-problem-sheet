# Square Root of a Number using Newton's method
# Author : Bashir Ahammed

fromUser = float(input("Please enter a positive number :"))
# Asking user for an input to find out the square root of
# We are type casting it for the float value

howMany = int (input("How many times need to calculate the approx :"))
""" We are also asking the user for another input to let us know 
for how many times to iterate in this method. This time it will be 
integer number 
"""

approx = 0.5*fromUser
#approx is a variable here

for i in range(howMany):
    betterapprox = 0.5*(approx + fromUser/approx)
    # betterapprox is an another variable to hold the final result of the equation
    
    approx = betterapprox


print ("The square root of 14.5 is approx. ",betterapprox)    
