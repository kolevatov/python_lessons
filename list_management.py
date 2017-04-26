# Управление списком значений.
# Поддерживает операции: добавить элемент, удалить элемент, распечатать список, сортировать, удалить дубликаты значений
#
scores = []
menu = None

while menu != '0':
    print("""
        0 - Выход
        1 - Добавить элемент
        2 - Удалить элемент
        3 - Распечатать список
        4 - Сортировать список
        5 - Удалить дубликаты элементов
    """)
    menu = input('Ваш выбор? ')
    print ('Выбран пункт: ', menu)
    if menu == '1':
        score = int(input('Новый элемент списка: '))
        scores.append(score)
    elif menu == '2':
        score = int(input('Удалить элемент со значением: '))
        if score in scores:
            scores.remove(score)
        else:
            print ('Элемента нет в списке!')
    elif menu == '3':
        print (scores)
    elif menu == '4':
        scores.sort()
    elif menu == '5':
        new_scores = []
        for i in scores:
            if i not in new_scores:
                new_scores.append(i)
        scores = new_scores
        new_scores = []
    elif menu == '0':
        None
    else:
        print ('Нет такого пукта меню!')
input('Нажмите любую кнопку. Программа будет завершена')




