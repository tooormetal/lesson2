

calendar = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень","Осень", "Осень", "Зима"]
choise = int(input("Введите номер месяца: "))
print(calendar[choise - 1])

calendar2 = {'1': 'Зима', '2': 'Зима','3': "Весна",'4': "Весна", '5': "Весна", '6': "Лето", '7': "Лето", '8': "Лето", '9': "Осень", '10': "Осень", '11': "Осень", '12': "Зима"}
choise2 = input("Введите номер месяца: ")
print(calendar2.get(choise2))
