from itertools import count, cycle
for el in count(10, 2):
    if el > 20:
        break
    else:
        print(el)

my_list = ['Имя', 'Фамилия', 'Город', 'Страна', 'Улица']
c = 0
for i in cycle(my_list):
    if c > 10:
        break
    else:
        print(i)
    c+=1

