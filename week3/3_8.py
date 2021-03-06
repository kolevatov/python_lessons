#   Система линейных уравнений - 1
"""
Даны вещественные числа a, b, c, d, e, f.
Известно, что система линейных уравнений:
ax + by = e
cx + dy = f
имеет ровно одно решение.
Выведите два числа x и y, являющиеся решением этой системы.

    Формат ввода
Вводятся шесть чисел a, b, c, d, e, f
- коэффициенты уравнений системы.
    Формат вывода
Выведите ответ на задачу.
"""
A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())

if B != 0:
    X = (B * F - D * E) / (B * C - A * D)
    Y = (E - A * X) / B
else:
    X = (D * E - B * F) / (A * D - C * B)
    Y = (F - C * X) / D

print('{0:.5f}'.format(X), '{0:.5f}'.format(Y))
