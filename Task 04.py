# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

import random
from collections import Counter

def Unique(list1):
    print(*Counter(list1))

Non_Unique = [random.randrange(1, 50, 1) for i in range(25)]
print(f'Random generated values are >>> {Non_Unique}')

print("\nThe unique values from list are")
Unique(Non_Unique)