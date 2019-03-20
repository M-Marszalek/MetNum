#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
import numpy as np

import matplotlib.pyplot as mp

print('Wprowadz punkt startowy wykresu:')
s=int(input())

print('Wprowadz dlugosc wykresu:')
l=int(input())

x = np.linspace(s, l+s, l*15)
y = ((x**3)-(5*x**2))*np.sin(x*2)

mp.plot(x, y, 'g')
