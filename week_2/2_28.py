#   Количество элементов, равных максимуму
"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, какое количество элементов этой последовательности,
равны ее наибольшему элементу.

    Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0
    Формат вывода
Выведите ответ на задачу.
"""
N = 1
max1 = 0
result = 0

while N != 0:
    N = int(input())

    if N > max1 and N != 0:
        max1 = N
        result = 1
    elif max1 == N and N != 0:
        result += 1

print(result)
