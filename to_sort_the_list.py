# Написать программу, которая получив на входе произвольный список удалит из него все повторяющиеся элементы.
lst = [1,3,2,3,4,5,4,6,7,9,8,9,35]
unique_list = []

for i in lst:
    if i not in unique_list: unique_list.append(i)
print (unique_list)
