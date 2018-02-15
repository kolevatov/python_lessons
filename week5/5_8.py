#   Диофантово уравнение - 2
"""
Даны числа a, b, c, d, e.
Подсчитайте количество таких целых чисел от 0 до 1000, которые являются
корнями уравнения (ax³+bx²+cx+d)/(x-e)=0,и выведите их количество.

    Формат ввода
Вводятся целые числа a, b, c, d и e.
    Формат вывода
Выведите ответ на задачу.
"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

result = 0

for x in range(0, 1001):
    if (A * (x**3) + B * (x**2) + C*x + D == 0) and (x - E != 0):
        result += 1
print(result)
