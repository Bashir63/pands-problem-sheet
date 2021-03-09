# Writing a program that takes a positive floating-point as input and outputs an approximation of its square root
# Here I have used the newton method to estimate the square roots

# Author : Bashir Ahammed
# Student ID : G00268666


fromUser = float(input("Please enter a positive number :"))
# Asking user for an input to find out the square root of
# We are type casting it for the float value

# Start of the function (called sqrt)
def sqrt(fromUser):

    #approx = the first number to test (= half the input number ( or half 14.5))
    approx = 0.5*fromUser

   # Start the loop for 20 times
    for i in range(20):
        
        #Newton's formula
        betterapprox = 0.5*(approx + fromUser/approx)
    
        #defining the new number to test for the next iteration
        approx = betterapprox

    # End the loop
    return betterapprox    

#best approx = the process of the function(sqrt)
bestapprox = (sqrt(fromUser))

#print the result of the function defined on the line above rounded to 1 decimal place 
print ("The square root of {} is approx. ".format(fromUser),round(bestapprox,1))    