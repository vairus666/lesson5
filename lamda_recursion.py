def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
 
x = input('Enter integer number\n')
while x:
    if isint(x):
        x = int(x)
        fact = lambda x: 1 if x == 0 else x * fact(x-1)    
        print(f'Factorial = {fact(x)}')
        break
    else:
        print(f"{x} can't integer number")
        x = input('Enter integer number\n')
