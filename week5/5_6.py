#   Лесенка
"""
По данному натуральному n≤9 выведите лесенку из n ступенек,
i-я ступенька состоит из чисел от 1 до i без пробелов.

    Формат ввода
Вводится натуральное число.
    Формат вывода
Выведите ответ на задачу.
"""
N = int(input())

for i in range(1, N+1):
    for j in range(1, i+1):
        print(j, sep='', end='')
    print('')