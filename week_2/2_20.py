#   Минимальный делитель
"""
Дано целое число, не меньшее 2.
Выведите его наименьший натуральный делитель, отличный от 1.

    Формат ввода
Вводится целое положительное число.
    Формат вывода
Выведите ответ на задачу.
"""
N = int(input())
i = 2
while (N % i != 0):
    i += 1
print(i)