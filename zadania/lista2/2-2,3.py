#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
import random as rn

x,y=3,3

while x%y != 0 or x%2 != 0 or y%2 != 0:
    x = rn.randrange(0, 100)
    y = rn.randrange(1, 10)
    print('X is divisible by Y' if x%y == 0 else "X isn't divisible by Y")
    xyEvenlog = 'X & Y are even' if x%2 == 0 and y%2 == 0 else "X & Y aren't even"
    print(xyEvenlog)

    
print(x,y)