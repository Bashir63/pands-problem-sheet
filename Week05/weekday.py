# Writing a program that outputs whether or not today is a weekday.
# The program allows to search the web to find out what day it is


# Student : Bashir Ahammed
# Student ID : G00268666

# For this program I'll have to import the datetime from the python library to find out what day it is
# Then I'll have to use the if/else statement to find out if it's a weekday or a weekend

# Importing datetime from the python library
from datetime import datetime
a = datetime.today().strftime('%A')

# In here if statement shows all the weekdays and it'll print accordingly if it's a week day and if it is not a week day it's a weekened where it will print by the else part of the statement
if a == "Monday" or a=="Tuesday" or a=="Wednesday" or a=="Thursday" or a=="Friday":
    # Here is a print method to check if that is a weekday 
    print("Yes, Unfortunately today is a weekday.")
else:
    # Here is a Print method to find out if it is a weekened today
    print("It is the weekend, Yay")  
