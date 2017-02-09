# Написать программу поиска самого длинного слова в строке, разделенной пробелами.

str = "Hello world a long string"
a=b=0
for i in str:
    if i is " ":
        if a>b: b=a
        a = 0
    else:
        a += 1
if a>b: b=a
print (b)