# Написать программу, выводящую заданную пользователем строку как минимум в 3 разных кодировках.

s = input("Строка для конвертации? ")
for i in map(lambda str: s.encode(str), ["koi8-r", "utf-8", "cp1251"]):
    print (i)