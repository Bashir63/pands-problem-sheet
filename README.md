# pands-problem-sheet
# GMIT, Galway

## Weekly Tasks of Programming and Scripting 

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

* https://www.w3school.com/python
* https://www.youtube.com/watch?v=TrP3gM0r2IE



## Week 03

# Task: Writing a program that takes asks a user to input a string and outputs every second letter in reverse order
Please enter a sentence: "The quick brown fox jumps over the lazy dog."
".o zletrv pu o wr cu h"


* First I have created the file for this task as secondstring.py
* In the task we have given a clue to take an user input which will be a string and
it will be sliced in a reverse way.
* Requests for a input which will be a string
* Then used the slice function in that string by [::-2] to get the expected output as the example showed in the task. 

# Code:

sentenceInput = (input ("Please enter a sentence: "))
sentencevalue = sentenceInput[::-2]
print(sentencevalue)


# Learning Outcome:

* Learned to work with a string.
* Learned to use the slice function.
* How to get back a string in a reverse way.


# References:

https://www.w3school.com/python










