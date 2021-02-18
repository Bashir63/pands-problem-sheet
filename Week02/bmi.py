# This is my first weekly problem solving program for this course
# This program calculates the user's BMI using their inputs
# Author : Bashir Ahammed


# inputs for user's height and weight

weight = float (input ("Enter weight: "))
height = float (input ("Enter height: ")) 

# Conversion of centimeters to meter squared
metersquared = (height / 100) **2

# Calculation of BMI
BMI = round(weight / metersquared, 2)

#BMI output
print("BMI is {}". format(BMI))