#2 ask the user for a number and print its factorial (1p)
y=1
print('Podaj liczbę całkowitą większą od zera')
x=int(input())
x1=x
while x>1:
    y=y*x    
    x=x-1
    
print('Silnia liczby ', x1 ,' to:',y)