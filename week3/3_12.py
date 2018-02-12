#   Второе вхождение
"""
Дана строка.
Найдите в этой строке второе вхождение буквы f и выведите индекс
этого вхождения.
Если буква f в данной строке встречается только один раз,
выведите число -1, а если не встречается ни разу, выведите число -2.
При решении этой задачи нельзя использовать метод count.

    Формат ввода
Вводится строка.
    Формат вывода
Выведите ответ на задачу.
"""
l_str = input()
pos1 = l_str.find('f')

if pos1 == -1:
    print(-2)
else:
    pos2 = l_str.find('f', pos1+1)
    print(pos2)
