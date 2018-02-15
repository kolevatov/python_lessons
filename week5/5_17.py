#   Ближайшее число
"""
Напишите программу, которая находит в массиве элемент,
самый близкий по величине к данному числу.

    Формат ввода
В первой строке задается одно натуральное число N, не превосходящее 1000 –
размер массива. Во второй строке содержатся N чисел – элементы массива
(целые числа, не превосходящие по модулю 1000).
В третьей строке вводится одно целое число x, не превосходящее по модулю 1000

    Формат вывода
Вывести значение элемента массива, ближайшее к X.
Если таких чисел несколько, выведите любое из них.
"""
N = int(input())
intList = list(map(int, input().split()))
X = int(input())

result = []

minDiff = 10000
result = 0
for i in range(0, len(intList)):
    if (intList[i] >= 0 and X >= 0) or (intList[i] < 0 and X < 0):
        if abs(intList[i] - X) < minDiff:
            minDiff = abs(intList[i] - X)
            result = intList[i]
    else:
        if abs(intList[i]) + abs(X) < minDiff:
            minDiff = abs(intList[i]) + abs(X)
            result = intList[i]
print(result)
