# Составить программу вывода таблицы умножения на число M
# Таблица составляется от M * a, до M * b, где M, a, b запрашиваются у пользователя.
print("Программа ввывода таблицы умножения на число M")
m = int(input("Введите число M: "))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

while a > b:
    print("a должно быть меньше b")
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))

while a <= b:
    print(m, "x", a, "=", m * a)
    a += 1
#