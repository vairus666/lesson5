#Factorial

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
 
n = input('Enter integer number\n')
while n:
    if isint(n):    
        print(fac(int(n)))
        break
    else:
        print("Enter can't integer number")
        n = input('Enter integer number\n')
