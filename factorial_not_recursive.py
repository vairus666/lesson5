from functools import reduce

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
 
n = input('Enter integer number\n')
while n:
    if isint(n):
        n = int(n)
        print (reduce(lambda x,y:x*y,range(1,n+1)))
        break
    else:
        print(f"{n} can't integer number")
        n = input('Enter integer number\n')
