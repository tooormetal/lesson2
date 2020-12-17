stop = ""
n = 0
list_items = []
while stop != "stop":
    name = input('введите название товара: ')
    price = input('введите стоимость товара: ')
    items = input("Введите количество товара:")
    dimen = input("Введите единицы измерения: ")
    stop = input("Чтобы добавить еще товар нажмите любую клавишу, для выхода введите stop: ")
    n = n + 1
    list_items.insert(n, name)
    features = {'название': name, 'цена': price, 'количество': items, 'измерение': dimen}


