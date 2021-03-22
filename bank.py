#Расчет суммы вклада в банк
from homework import helping

def contribution(a, b ,c):
    # Вычисление суммы 
    d = 0
    while c > 0:
        d = (d+d*b*0.01)+a
        c -= 1
    return d
invest = percent = mouth = 0
emp =''
while invest != emp or percent != emp or mouth != emp:
    invest = input('Введите сумму вклада\n')
    if  helping.isint(invest):
        percent = input('Введите количество процентов\n')
        if helping.isfloat(percent):
            mouth = input('Ведите количество месяцев\n')
            if helping.isint(mouth):
                invest = int(invest)
                percent = float(percent)
                mouth = int(mouth)
                print(f"результат вклада {contribution(invest,percent,mouth): .2f}")
            elif mouth == emp:
                print('вы  не ввели первую переменную так что пока')
                break
            else:
                print('Введено неправильное значение количества месяцев')
        elif percent == emp:
            print('вы  не ввели первую переменную так что пока')
            break                        
        else:
            print('Введено неправильное значение количества процентов')
    elif invest == emp:
        print('вы  не ввели первую переменную так что пока')
        break
    else:
        print('Введена неправильная значение суммы вклада')
           