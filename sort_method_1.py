# Сортировка списка "пузырьком"
import random

lst = list(range(25))
random.shuffle(lst)
j = 0
flag = True

print ("Initial list", lst)

while (flag):
    flag = False
    for i in range(len(lst)-1):
        if (lst[i] > lst[i+1]):
            j = lst[i+1]
            lst[i+1] = lst[i]
            lst[i] = j
            flag = True

print ("Result list", lst)
