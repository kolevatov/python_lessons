#   Словарь синонимов
"""
Вам дан словарь, состоящий из пар слов.
Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.
Для одного данного слова определите его синоним.

    Формат ввода
Программа получает на вход количество пар синонимов N.
Далее следует N строк, каждая строка содержит ровно два слова-синонима.
После этого следует одно слово.
    Формат вывода
Программа должна вывести синоним к данному слову.
"""
finput = open('input.txt', 'r', encoding='utf-8')

N = int(finput.readline())

syn = {}

for i in range(N):
    key, value = finput.readline().split()
    syn[key] = value
    syn[value] = key

word = (finput.readline()).strip()
print(syn[word])
