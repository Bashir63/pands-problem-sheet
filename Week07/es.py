# Writing a program that reads in a text file and outputs the number of e's it conditions
# Student : Bashir Ahammed
# Student ID : G00268666

# At the begining, we are importing sys to take the filename from an argument on the command line
  
import sys

filename = sys.argv[1]

# Opening the file with the keywords "with open", so that the file gets closed automatically
# And using 'r', to open the file in read mode 

with open(filename, 'r') as f:
    
    # Here "data" is a variable to read the command line file
    data = f.read()
   
   # Here 'Es' is another variable to hold the results we are looking for
    Es = data.count("e")

# Finally we are printing the results with the print function
print(Es)    

