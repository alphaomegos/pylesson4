# Реализовать два небольших скрипта:
#
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

import time
from itertools import count, cycle

Start = int(input('Enter start number >>> '))

for el in count(int(Start)):
    print(el)
    if el > Start ** 4:
        break

N = int(input("\nEnter minutes for timeout >>> "))
Timeout = time.time() + 60 * N  # N minutes from now
Input_List = input('Enter elements. Separate them by space. Finish with enter.')
for el in cycle(Input_List):
    print(el)
    if time.time() > Timeout:
        break