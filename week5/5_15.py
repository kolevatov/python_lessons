#   Наименьший положительный
"""
Выведите значение наименьшего из всех положительных элементов в списке.
Известно, что в списке есть хотя бы один положительный элемент,
а значения всех элементов списка по модулю не превосходят 1000.

    Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
    Формат вывода
Выведите ответ на задачу.
"""
N = list(map(int, input().split()))
rMin = 1001

for i in range(len(N)):
    if (N[i] < rMin) and (N[i] > 0):
        rMin = N[i]
print(rMin)