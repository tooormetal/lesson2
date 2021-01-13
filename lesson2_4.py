string = input("Введите строку: ")
list = string.split()
for i in list:
    if len(i) < 10:
        print(i)
    else:
        print(i[0: 10])