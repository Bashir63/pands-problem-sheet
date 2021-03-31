# Writing a program that asks the user to input any positive integer and outputs the successive values of a calculation
# At each step calculating the next value by taking the current value
# For even number, will be divided by two
# For odd number, will be multiplied by three and added one
# Ending the program when the current valer is one


# Student: Bashir Ahammad
# Student ID: G00268666


#References :

#Andrew Beaty, Lecturer, Programming and Scripting lecture presentation
#https://www.youtube.com
#https://www.w3school.com/python
#https://www.github.com


#Taking input from user
n = int( input("Please input a positive integer "))

# Using the while loop to check if the input (n) is not equelty one 
while n != 1:
    # Using the if statement to check the number even or odd by dividing by two
    if n % 2 == 0:
        n = n/2
    # Using the else statement if the number is odd which will be multiplied by three and added one 
    else:
        n = 3*n+1
    
    # Finally using the round method and printing the results
    print (round(n)) # n is the input here 
