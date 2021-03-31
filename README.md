# pands-problem-sheet
# GMIT, Galway

# Weekly Tasks of Programming and Scripting 

## Name: Bashir Ahammed 
## Student ID: G00268666


# Week 1:

Install Softwares and Create Repositories


# Week 2:

Task: Writing a program that calculates sombody's Body Mass Index (BMI). 

First I have created the file for this task as bmi.py
The first input is the person's height in centimeters and the second input is the weight in kilograms. Both inputs I have type casted as float so that I can work with the decimel points.
Body Mass Index (BMI) is a person’s weight in kilograms divided by the square of height in meters.

The code I have used there are shown below:

weight = float (input ("Enter weight: "))
height = float (input ("Enter height: ")) 
metersquared = (height / 100) **2
BMI = round(weight / metersquared, 2)
print("BMI is {}". format(BMI))

Learning Outcome:

* Learned how to take user input for the particular programing
* Learned how to search for a references on the web
* How to do the calculation in the programming

References:

* Andrew Beaty, Lecturer, Programming and Scripting lecture presentation
* https://www.w3school.com/python
* https://www.youtube.com/watch?v=TrP3gM0r2IE
* https://www.github.com



# Week 03

Task: Writing a program that takes asks a user to input a string and outputs every second letter in reverse order

Please enter a sentence: "The quick brown fox jumps over the lazy dog."
".o zletrv pu o wr cu h"


* First I have created the file for this task as secondstring.py
* In the task we have given a clue to take an user input which will be a string and
it will be sliced in a reverse way.
* Requests for a input which will be a string
* Then used the slice function in that string by [::-2] to get the expected output as the example showed in the task. 

## Code:

sentenceInput = (input ("Please enter a sentence: "))
sentencevalue = sentenceInput[::-2]
print(sentencevalue)


## Learning :

* Learned to work with a string.
* Learned to use the slice function.
* How to get back a string in a reverse way.


## References:

Andrew Beaty, Lecturer, Programming and Scripting lecture presentation
https://www.w3school.com/python
https://www.github.com




# Week 04

 Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
 At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one
 Have the program end if the current value is one.


* First I have created a file for this task as collatz.py
* Begening of the programm, I have created a function for an user input which will be a positive integer
* I had to convert that input to an integer, otherwise python will recognise it as a string


## Code:

n = int( input("Please input a positive integer "))
while n != 1:
if n % 2 == 0:
        n = n/2
 else:
    n = 3*n+1
print (round(n))   


## Learning :

* Learning how to use while loop and checking if the input (n) is not equelty one by the while loop
* Being introduced with the if/else statements in the following lines
* Using the if statement to check the number even or odd by dividing by two
* Using the else statement if the number is odd which will be multiplied by three and added one 
* At the end, using the round method and printing the results



# References :

Andrew Beaty, Lecturer, Programming and Scripting lecture presentation
https://www.youtube.com
https://www.w3school.com/python
https://www.github.com




# Task :  Writing a program that outputs whether or not today is a weekday. The program allows to search the web to find out what day it is

* For this program, I have created a file called weekday.py 
* Begining of the program I have imported the datetime library which is a python library to find out what day it is
* Then I have used the conditional if/else statement to find out if it's a weekday or a weekend

# Code :

from datetime import datetime
a = datetime.today().strftime('%A')
if a == "Monday" or a=="Tuesday" or a=="Wednesday" or a=="Thursday" or a=="Friday":
print("Yes, Unfortunately today is a weekday.")
else:
print("It is the weekend, Yay") 


# Learning :

* Started learning how to use python librayries
* In the first code block, "if" statement shows all the weekdays and if the date time library shows it's a week day then it'll print accordingly
* if it is not a week day, the code will go to the else block and will print "It is the weekend, Yay" 


* References :

Andrew Beaty, Lecturer, Programming and Scripting lecture presentation
https://www.github.com
https://www.w3school.com/python
https://www.youtube.com/watch?v=jx8y647CMsI&t=299s






# Task : 

Writing a program that takes a positive floating-point as input and outputs an approximation of its square root

* The file I have created for this program is squareroot.py
* Here I have used Newton's method to estimate the square roots
* Firstly asking the user for an input to find out the square root of
* We are type casting it for the float value
* defining a function at the begining t (called sqrt)


* Code:

fromUser = float(input("Please enter a positive number :"))
def sqrt(fromUser):
approx = 0.5*fromUser
betterapprox = 0.5*(approx + fromUser/approx)
approx = betterapprox
return betterapprox    
bestapprox = (sqrt(fromUser))
print ("The square root of {} is approx. ".format(fromUser),round(bestapprox,1))


Learning :

* Newton's method :
Start with an initial approximation x0 close to c.
Determine the next approximation by the formula x1=x0−f(x0)f′(x0).
Continue the iterative process using the formula xn+1=xn−f(xn)f′(xn) until the root is found to the desired accuracy.
* 



