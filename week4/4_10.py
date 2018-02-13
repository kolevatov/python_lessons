#   Сократите дробь
"""
Даны два натуральных числа n и m.
Сократите дробь (n / m), то есть выведите два других числа p и q таких,
 что (n / m) = (p / q) и дробь (p / q) — несократимая.

Решение оформите в виде функции ReduceFraction(n, m),
получающая значения n и m и возвращающей кортеж из двух чисел (return p, q)
    Формат ввода
Вводятся два натуральных числа.
    Формат вывода
Выведите ответ на задачу.
"""


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def ReduceFraction(n, m):
    div = gcd(n, m)
    return (n // div, m // div)

A = int(input())
B = int(input())

p, q = ReduceFraction(A, B)
print(p, q)
