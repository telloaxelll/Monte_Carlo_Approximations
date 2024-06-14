"""
Part 1: Mathematical Computation of Monte Carlo 
"""

# Needed modules
import numpy as np
import matplotlib.pyplot as plt

# Lists that store the points that are inside the
# unit cirlce (<= 1).
data_x = []
data_y = []

# Possible cases of N -> ∞ that test the accuracy of the code. 
ten = 10 
thousand = 1_000
hundred_thousand = 100_000
million = 1_000_000

# True counter to count total amount of indications that randomized (x,y) points are
# witin the unit circle. 
t = 0

# Monte Carlo simulation code
for trial in range (hundred_thousand):
    # Generate data betweem [-1, 1] since we have denoted as the center of the graph as (0,0),
    # therefore the unit circle forces us to take in values from quadrant 2, 3, and 4. 
    x = np.random.uniform(-1, 1) # Note: "np.random.uniform" = submodule within a module 
    y = np.random.uniform(-1, 1) # Note: "np.random.uniform" = submodule within a module 

    # Activation function to determine points that 
    # are inside the unit circle
    if ((x ** 2) + (y ** 2)) <= 1:
        t += 1
        data_x.append(x)
        data_y.append(y)


# If we were to change the amount of trials that we were to do, we'd still get the same thing just appoximated at
# a more accurate degree. See below for different cases 
print(f'Tested under {hundred_thousand} samples: {t}/{hundred_thousand} = {(4 * t)/hundred_thousand}')


""" 
Part 2: Monte Carlo Visualization 
"""
# Desgining grid 
plt.figure(figsize = (10, 10))
plt.scatter(data_x, data_y, color = 'green', s=1)
plt.xlabel('domain')
plt.ylabel('range')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()
