#Calc

def calc(a, b, operation):
    
    def add(a1, b1):

        return a1 + b1

    def remove(a1, b1):
        return a1 - b1

    def multiply(a1, b1):
            return a1 * b1
    def divide(a1, b1):
        return a1 / b1

    def power(a1, b1):
        return a1 ** b1

    def root(a1):
        return a1 ** .5

    selector = {
    "+": add,
    "-": remove,
    "*": multiply,
    "/": divide,
    "^": power,
    "√": root
    }

    return selector[operation](a, b)


def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

selector = {"+", "-", "*", "/", "^", "√"}
x = input('Введите первое значение\n')
oper = input('Введите операцию (+, -, /, *, ^, √)\n')
y = input('Введите второе значение\n')
if isfloat(x):
    if oper in selector:
        if isfloat(y):
                print(f'Результат равен = {calc(float(x),float(y), oper):.3f}')
        else:
            print(f'{y} не число')   
    else:
        print(f'{oper} - такая операция мне не известна')
else:
    print(f'{x} не число')
