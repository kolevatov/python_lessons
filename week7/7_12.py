#   Частотный анализ
"""
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую
строку. Слова должны быть отсортированы по убыванию их количества появления
в тексте, а при одинаковой частоте появления — в лексикографическом порядке.

    Указание.
После того, как вы создадите словарь всех слов, вам захочется отсортироватьего
по частоте встречаемости слова. Желаемого можно добиться, если создать список,
элементами которого будут кортежи из двух элементов: частота встречаемости
слова и само слово.
Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
Тогда стандартная сортировка будет сортировать список кортежей, при этом
кортежи сравниваются по первому элементу, а если они равны —то по второму.
Это почти то, что требуется в задаче.

    Формат ввода
Вводится текст.
    Формат вывода
Выведите ответ на задачу.
"""
finput = open('input.txt', 'r', encoding='utf-8')

text = list(finput.read().split())
words = {}
for key in text:
    words[key] = words.get(key, 0) + 1

text = []
for key in words:
    text.append((-words[key], key))

text.sort()
for i in text:
    print(i[1])