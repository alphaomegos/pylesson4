# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import functools

Even_List = list(filter(lambda i: (i % 2 == 0), range(100, 1001)))
print(Even_List)

print("\nThe multiplication of all elements is : ",end="")
print(functools.reduce(lambda a,b : a*b, Even_List))