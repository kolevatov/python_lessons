#   Дележ яблок-2
# N школьников делят K яблок поровну,
# не делящийся остаток остается в корзинке.
# Сколько яблок останется в корзинке?
#   Формат ввода
# Программа получает на вход числа N и K — натуральные, не превышают 10000.
#   Формат вывода
# Выведите ответ на задачу.

N = int(input())
K = int(input())

print(K % N)