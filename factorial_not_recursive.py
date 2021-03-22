# Вычисление факториала без рекурсии
from functools import reduce
from homework import helping
 
n = input('Enter integer number\n')
while n:
    if helping.isint(n):
        n = int(n)
        print (reduce(lambda x,y:x*y,range(1,n+1)))
        break
    else:
        print(f"{n} can't integer number")
        n = input('Enter integer number\n')
