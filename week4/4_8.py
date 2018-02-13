#   Сложение без сложения
"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

    Формат ввода
Вводятся два целых числа.
    Формат вывода
Выведите ответ на задачу.
"""


def sum(a, b):
    if b > 0:
        return sum(a+1, b-1)
    return a

A = int(input())
B = int(input())
print(sum(A, B))