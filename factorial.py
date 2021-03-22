#Вычисление факториала
from homework import helping

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

n = input('Enter integer number\n')
while n:
    if helping.isint(n):    
        print(fac(int(n)))
        break
    else:
        print(f"{n} can't integer number")
        n = input('Enter integer number\n')
