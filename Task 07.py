# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial

def Fact_Gen():
    for el in count(1):
        yield factorial(el)

Gen_List = Fact_Gen()
x = 0
Max = int(input("Enter restriction number >>> "))
for i in Gen_List:
    if x < Max:
        print(i)
        x += 1
    else:
        break