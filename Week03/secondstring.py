
# A string in every second letter in reverse order
# Author: Bashir Ahammed


sentenceInput = (input ("Please enter a sentence: "))
sliceValue = slice(sentenceInput[::-2])

print('{}'.format(sliceValue))