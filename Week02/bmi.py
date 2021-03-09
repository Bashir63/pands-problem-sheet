# Writing a program that calculates sombody's Body Mass Index (BMI)

# Author : Bashir Ahammed


# First I'll write a program two take two inputs from the users. As this inputs will be an integer, I'll convert this into float by type casting 
  


# This first input is the person's height in centimeters which is type casted into floats
weight = float (input ("Enter weight: "))


#This second input is the person's weight in kilograms 
height = float (input ("Enter height: ")) 


# Conversion of centimeters to meter squared by this method 
metersquared = (height / 100) **2

# Calculation of BMI
BMI = round(weight / metersquared, 2)

#BMI output
print("BMI is {}". format(BMI))