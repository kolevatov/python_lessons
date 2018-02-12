#   Проценты
"""
Процентная ставка по вкладу составляет P процентов годовых,
которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.
Определите размер вклада через год. При решении этой задачи нельзя
пользоваться условными инструкциями и циклами.

    Формат ввода
Программа получает на вход целые числа P, X, Y.
    Формат вывода
Программа должна вывести два числа: величину вклада через год в
рублях и копейках. Дробная часть копеек отбрасывается.
"""
P = int(input())
X = int(input())
Y = int(input())

amount = X + Y / 100
amount += (amount * P) / 100

A = int(amount)
B = int((amount - A) * 100 + 0.00001)
print(A, B)
