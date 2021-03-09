# Writing a program that asks the user to input any positive integer and outputs the successive values of a calculation
# At each step calculating the next value by taking the current value
# For even number, will be divided by two
# For odd number, will be multiplied by three and added one
# Ending the program when the current valer is one


# Author: Bashir Ahammad
# Student ID: G00268666


#Taking input from user
n = int( input("Please input a positive integer "))

# Using the while loop to check if the input (n) is equelty one 
while n != 1:
    # Using the if statement to check the number even or odd by dividing by two
    if n % 2 == 0:
        n = n/2
    # Using the else statement if the number is odd which will be multified by three and added one 
    else:
        n = 3*n+1
    # Finally using the round method to get the integer results and printing the results
    print (round(n)) # n is the input here 
