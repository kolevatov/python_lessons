#   Симметричное число
# Дано четырехзначное число.
# Определите, является ли его десятичная запись симметричной.
# Если число симметричное, то выведите 1,
# иначе выведите любое другое целое число.
# Число может иметь меньше четырех знаков,
# тогда нужно считать, что его десятичная запись
# дополняется слева незначащими нулями.
#   Формат ввода
# Вводится единственное число.
#   Формат вывода
# Выведите ответ на задачу.

N = int(input())
n1 = N // 1000
n2 = (N - n1 * 1000) // 100
n3 = (N - n1 * 1000 - n2 * 100) // 10
n4 = N - n1 * 1000 - n2 * 100 - n3 * 10
n12 = int(str(n1) + str(n2))
n23 = int(str(n4) + str(n3))
result = 1 + (n12 - n23)

print(result)
