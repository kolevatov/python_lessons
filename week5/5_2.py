#   Ряд - 2
"""
Даны два целых числа A и В. Выведите все числа от A до B включительно,
в порядке возрастания,если A < B, или в порядке убывания в противном случае.

    Формат ввода
Вводятся два целых числа.
    Формат вывода
Выведите ответ на задачу.
"""
A = int(input())
B = int(input())
iterator = 1

if A > B:
    iterator = -1

for i in range(A, B+iterator, iterator):
    print(i, end=" ")
