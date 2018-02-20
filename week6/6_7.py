#   Сортировка подсчетом
"""
Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения
от 0 до 100.
Отсортируйте этот список в порядке неубывания элементов.
Выведите полученный список.
"""
inputStream = list(map(int, input().split()))
tmpList = [0]*101

for i in inputStream:
    tmpList[i] += 1

inputStream = []

for i in range(len(tmpList)):
    if tmpList[i] > 0:
        print((str(i) + ' ') * tmpList[i], end='')
