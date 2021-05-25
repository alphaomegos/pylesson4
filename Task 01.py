# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def Salary():
    try:
        Hours = float(input('Enter working hours >>> '))
        Payrate = float(input('Enter payrate per hour >>> '))
        Bonus = float(input('Enter bonus >>> '))
        Result = Hours * Payrate + Bonus
        print(f'Final salaty is >>> {round(Result)}')
    except ValueError:
        return print('Data should be a number')

Salary()