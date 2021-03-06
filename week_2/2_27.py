#   Второй максимум
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение второго по величине элемента в этой последовательности,
то есть элемента, который будет наибольшим, если из последовательности
удалить одно вхождение наибольшего элемента.

    Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0
    Формат вывода
Выведите ответ на задачу.
"""
N = 1
max1 = 0
max2 = 0

while N != 0:
    N = int(input())

    if N > max1 and N != 0:
        max2 = max1
        max1 = N
    else:
        if N > max2 and N != 0:
            max2 = N

print(max2)
