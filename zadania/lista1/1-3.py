#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
import numpy as np
import random as rd

def mini(x):
    print(x.min())
    for i in range(int((np.size(x)/len(x)))):
        for j in range(len(x)):
            if x[j,i]== x.min():
                print('najmniejsza wartosc to:',x.min(),' i znajduje sie w miejscu o indeksie:',i,',',j)
                
        
x=np.zeros([12,34])

for i in range(int((np.size(x)/len(x)))):
    for j in range(len(x)):
        x[j,i]=rd.randint(10,500)
print(x)

mini(x)