#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cs50 as cs

q = cs.get_float('q = ')
x_knots = np.linspace(-3*np.pi,3*np.pi,201)
y_knots = np.linspace(-3*np.pi,3*np.pi,201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+Y**2)*q
Z = np.cos(R)**2*np.exp(-0.1*R)
ax = Axes3D(plt.figure(figsize=(10,10)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.rainbow, linewidth=4)
plt.show()