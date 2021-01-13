with open("text.txt", "w", encoding="utf-8") as moon:
    while str != "":
        str = input("Введите строку для записи:")
        print(str, file=moon)