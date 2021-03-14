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
x = oper = y = 0
emp =''
while x != emp or oper != emp or y != emp:
    x = input('Введите первое значение\n') 
    if isfloat(x):
        oper = input('Введите операцию (+, -, /, *, ^, √)\n')
        if oper in selector:
            y = input('Введите второе значение\n')
            if isfloat(y):
                try:
                    print(f'Результат равен = {calc(float(x),float(y), oper):.3f}')
                    x = input('Введите первое значение\n')
                    oper = input('Введите операцию (+, -, /, *, ^, √)\n')
                    y = input('Введите второе значение\n')
                except Exception as e:
                    print('Error!!!' + str(e))
                    print('Введите пример заново')
                    x = input('Введите первое значение\n')
                    oper = input('Введите операцию (+, -, /, *, ^, √)\n')
                    y = input('Введите второе значение\n')
            elif y == emp:
                print('вы  не ввели вторую переменную так что пока')
                break
            else:
                print(f'{y} не число')
                print('Введите пример заново')
                x = input('Введите первое значение\n')
                oper = input('Введите операцию (+, -, /, *, ^, √)\n')
                y = input('Введите второе значение\n')   
        elif oper == emp:
            print('вы  не ввели операцию так что пока')
            break
        else:
            print(f'{oper} - такая операция мне не известна')
            print('Введите пример заново')
            x = input('Введите первое значение\n')
            oper = input('Введите операцию (+, -, /, *, ^, √)\n')
            y = input('Введите второе значение\n')
    elif x == emp:
        print('вы  не ввели первую переменную так что пока')
        break
    else:
        print(f'{x} не число')
        print('Введите пример заново')
        x = input('Введите первое значение\n')
        oper = input('Введите операцию (+, -, /, *, ^, √)\n')
        y = input('Введите второе значение\n')
