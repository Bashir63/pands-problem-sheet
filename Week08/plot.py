import numpy as np
import matplotlib.pyplot as plt

# Create the vectors X and Y
x = np.array(range(0,4))
y = x 

a = np.array(range(0,4))
b = x*x

c = np.array(range(0,4))
d= x*x*x


# Create the plot
plt.plot(x,y)
plt.plot(a,b)
plt.plot(c,d)

# Show the plot
plt.show()