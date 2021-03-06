#   Проверка на делимость
# В этой задаче необходимо проверить,
# делится ли число A на число B нацело.
# Использовать можно только арифметические операции,
# использование любых видов ветвлений, функций и т.п. запрещено.
#   Формат ввода
# Вводятся два натуральных числа A и B.
#   Формат вывода
# Выведите "YES", если A кратно B и "NO" в противном случае.
A = int(input())
B = int(input())

result = 'YES' * int((A % B) == 0) + 'NO' * int((A % B) != 0)
print(result)
