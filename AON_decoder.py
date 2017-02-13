# Написать программу декодирования телефонного номера для АОН.
"""
По запросу АОНа АТС посылает телефонный номер, используя следующие правила:
— Если цифра повторяется менее 2 раз, то это помеха и она должна быть отброшена
— Каждая значащая цифра повторяется минимум 2 раза
— Если в номере идут несколько цифр подряд, то для обозначения «такая же цифра как предыдущая» используется идущий 2 или более подряд раз знак #

Например, входящая строка 4434###552222311333661 соответствует номеру 4452136
"""
#src = "22122"
#src = "4434###552222311333661"
src = "###4434###552222311333661"
dst = ""
last = ""

print ("Запрос: ", src)
i = 0

while i<len(src)-1:
    #print (i, "pos: ", src[i])
    if (src[i] is src[i+1]) and not(src[i] is last):
        dst = dst + src[i]
        last = src[i]
    elif not (src[i] is src[i+1]) and not(src[i] is last):
        last = ""
    i += 1

#print ("Ответ: ", dst)

i = 0
while i<len(dst):
    if (dst[i] is "#") and (i>0):
        dst = dst[:i] + dst[i-1] + dst[i+1:]
    elif (dst[i] is "#"):
        dst = dst[i+1:]
    i += 1

print ("Ответ: ", dst)