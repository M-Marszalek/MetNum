#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
import numpy as np
p=56
k=100
l=k-p+1

def funk(x):
    y = 2*x**2+2*x+2
    print('For x=', x ,'y= ', y)   
    
for i in range(l):
   funk(i+p)

