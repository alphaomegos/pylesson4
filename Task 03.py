# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print(f'Numbers from 20 to 240 divisible by 20 or 21 >>> {list(filter(lambda i: (i % 20 == 0 or i % 21 == 0), range(20, 241)))}')


