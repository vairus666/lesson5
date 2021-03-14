#Bank

def contribution(a, b ,c):
        d = 0
        while c > 0:
                d = (d+d*b*0.01)+a
                c -= 1
        return d

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


invest = input('Введите сумму вклада\n')
percent = input('Введите количество процентов\n')
mouth = input('Ведите количество месяцев\n')
if isint(invest):
        if isfloat(percent):
                if isint(mouth):
                        invest = int(invest)
                        percent = float(percent)
                        mouth = int(mouth)
                        print(f"результат вклада {contribution(invest,percent,mouth): .2f}")
                else:
                        print('Введено неправильное значение количества месяцев')                        
        else:
                print('Введено неправильное значение количества процентов')
else:
        print('Введена неправильная значение сумма вклада')
