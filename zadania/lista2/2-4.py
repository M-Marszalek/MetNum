#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)

import cs50 as cs

x = cs.get_float('x = ')
y = cs.get_float('y = ')
while y == 0:
    print(' nie mozna dzielic przez 0 podaj inna liczbe')
    y = cs.get_float('y = ')

print(x/y)
w = x/y
print(round(w,2))
print("%.2f" % w)