#   Последняя цифра
# Дано натуральное число. Выведите его последнюю цифру.
#   Формат ввода
# Вводится единственное целое неотрицательное число
# (гарантируется, что оно не превышает 10000).
#   Формат вывода
# Выведите ответ на задачу.

N = int(input())
res = N - (N // 10) * 10
print(res)