# Collatz number exercise
# Author: Bashir Ahammad

# I had to watch some of the youtube videos to understand what is the Collatz number about
# This code will be updated as I am trying to learn more of coding

#Taking input from user
n = int( input("Please input a positive integer "))
# using while loop
while n != 1:
    if n % 2 == 0: # using if statement to check the number even or odd
        n = n/2
    else:
        n = 3*n+1
    print(n) # n is the input here 