#   Замечательные числа - 1
"""
Найдите и выведите все двузначные числа,
которые равны удвоенному произведению своих цифр.

    Формат ввода
Программа не требует ввода данных с клавиатуры,
просто выводит список искомых чисел.
    Формат вывода
Выведите ответ на задачу.
"""


def proc(n):
    a = n // 10
    b = n % 10
    return a, b

for i in range(10, 100):
    A, B = proc(i)
    if i == A * B * 2:
        print(i, end=' ')
