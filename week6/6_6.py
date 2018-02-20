#   Отсортировать список участников по алфавиту
"""
Известно, что фамилии всех участников — различны.
Сохраните в массивах список всех участников и выведите его,
отсортировав по фамилии в лексикографическом порядке.
При выводе указываете фамилию, имя участника и его балл.
"""
finput = open('input.txt', 'r', encoding='utf-8')
foutput = open('output.txt', 'w', encoding='utf-8')

participants = []

for i in finput:
    line = i.split()
    participants.append(line[0] + ' ' + line[1] + ' ' + line[3])

participants.sort()
for i in participants:
    print(i, file=foutput)
foutput.close()
