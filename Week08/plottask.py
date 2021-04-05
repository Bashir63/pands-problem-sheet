# Writing a program which displays a plot of the functions f(x)=x, g(x)=x*x and h(x)=x*x*x in the range [0, 4] on the one set axes

# Student : Bashir Ahammed
# Student ID : G00268666


#References :

    #Andrew Beaty, Lecturer, Programming and Scripting lecture presentation
    #https://www.github.com
    #https://www.w3school.com/python/matplotlib_plotting.asp
    #https://www.youtube.com/watch?v=uIW5Hi17jO0


# Importing a python library called numpy as np to perform the array functions and 
# importing python library called matplotlib as plt to draw the plots

import numpy as np
import matplotlib.pyplot as plt


plt.ylim(0,80)

# Create the vectors X and Y
x = np.array(range(0,5))
y = x 

a = np.array(range(0,5))
b = x*x

c = np.array(range(0,5))
d= x*x*x


# Using the marker function to emphasize the each points with a different specified marker
plt.plot(x,y, marker = '*')
plt.plot(a,b, marker = 'o')
plt.plot(c,d, marker = 'P')

# Using the title function to name the plot 
plt.title("Value of f(x)=x,  g(x)=x^2,  h(x)=x^3")
# Using the label function to set a label for the x- and y-axis
plt.xlabel("x-axis")
plt.ylabel("y-axis")
#Using the grid function to add grid lines to the plot
plt.grid(color = 'red', linestyle = '--', linewidth = 0.5)

# Show the plot
plt.show()

