#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
import math as mt
from cs50 import *

def perimeter(r):
    l=2*r*mt.pi
    return(l)
    
def field(r):
    p = mt.pi*r**2
    return (p)

x = get_float('x: ')
y = get_float('y: ')

if x<0:
    print('dla podanego x pole i dlugosc nie istnieje')
else:
    print('dla podanego x pole = ', field(x),' a dlugosc =', perimeter(x))

if y<0:
    print('dla podanego y pole i dlugosc nie istnieje')
else:
    print('dla podanego y pole = ', field(y),' a dlugosc =', perimeter(y))

