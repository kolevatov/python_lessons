#   Ряд - 3
"""
Дано натуральное число n.
Напечатайте все n-значные нечетные натуральные числа в порядке убывания.

    Формат ввода
Вводится натуральное число.
    Формат вывода
Выведите ответ на задачу.
"""
N = int(input())

for i in range(10**N - 1, 10**(N-1) - 1, -2):
    print(i, end=" ")