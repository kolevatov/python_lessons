#   Четные и нечетные
"""
Даны три целых числа A, B, C.
Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.
Формат ввода
    Числа A, B, C, не превышающие по модулю 10000.
Формат вывода
    Одна строка – "YES" или "NO".
"""
A = int(input())
B = int(input())
C = int(input())

if (A % 2 == 0) or (B % 2 == 0) or (C % 2 == 0):
    if (A % 2 != 0) or (B % 2 != 0) or (C % 2 != 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
