my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []
[new_list.append(el) for el in my_list if el not in new_list]
print(new_list)