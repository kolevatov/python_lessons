#   Коровы
# Для данного числа n<100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”, “n коровы”,
# правильно склоняя слово “корова”.
#   Формат ввода
# Вводится натуральное число.
#   Формат вывода
# Программа должна вывести введенное число n и одно из слов:
# korov, korova или korovy.
# Между числом и словом должен стоять ровно один пробел.
N = int(input())
diff = N % 10
if (diff == 1) and (N != 11):
    print(N, 'korova')
elif diff in [2, 3, 4] and N not in [12, 13, 14]:
    print(N, 'korovy')
else:
    print(N, 'korov')