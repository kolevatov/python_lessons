#   Сумма квадратов
"""
По данному натуральном n вычислите сумму 1²+2²+3²+...+n².

    Формат ввода
Вводится натуральное число.
    Формат вывода
Выведите ответ на задачу.
"""
N = int(input())
result = 0

for i in range(1, N + 1):
    result += i**2
print(result)