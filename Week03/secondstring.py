
# Writing a program that takes asks a user to input a string and outputs every second letter in reverse order

# Student: Bashir Ahammed
# Student ID: G00268666

# Asking the user for an input which will be a string
sentenceInput = (input ("Please enter a sentence: "))

# Method to reverse the every second letter of the user's string
sentencevalue = sentenceInput[::-2]

# Finally using printing method to display the result of the program
print(sentencevalue)