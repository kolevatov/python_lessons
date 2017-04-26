list_1 = ['aaa','bbb','ccc']
list_2 = list_1
list_3 = list_1[:]
print ('1 - ',list_1)
print ('2 - ',list_2)
print ('3 - ',list_3)
list_3.append('ddd')
print('1 - ', list_1)
print ('3 - ',list_3)