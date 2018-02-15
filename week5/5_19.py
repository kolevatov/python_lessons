#   Переставить min и max
"""
В списке все элементы различны.
Поменяйте местами минимальный и максимальный элемент этого списка.

    Формат ввода
Вводится список целых чисел. Все числа списка находятся на одной строке.
    Формат вывода
Выведите ответ на задачу.
"""
N = list(map(int, input().split()))
min = N[0]
max = N[0]
result = []

for i in N:
    if i > max:
        max = i
    elif i < min:
        min = i

for i in N:
    if i == min:
        result.append(max)
    elif i == max:
        result.append(min)
    else:
        result.append(i)
print(*result)
