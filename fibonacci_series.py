# Ряд Фибоначчи
# Каждый следующий элемент равен сумме двух предыдущих

a,b = 0,1
n1 = int(input("Elements? "))
n2 = 0
while n2 < n1:
    print(a)
    a,b = b,a+b
    n2 += 1


