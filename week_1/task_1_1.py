# Напишите программу, которая приветствует пользователя, выводя слово Hello,
# введенное имя и знаки препинания по образцу.
# Программа должна считывать в строковую переменную значение и
# писать соответствующее приветствие.
# Обратите внимание, что после запятой должен обязательно стоять пробел,
# а перед восклицательным знаком пробела нет.
# Операцией конкатенации строк (+) пользоваться нельзя.
# Пример:
#   Тест 1
#   Входные данные:
#   Harry
#   Вывод программы:
#   Hello, Harry!

str = input()
print('Hello,', str, end='!')
