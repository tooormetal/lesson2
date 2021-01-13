with open("text_3.txt", "r", encoding="utf-8") as pay:
    new_list = pay.readlines()
    midle = 0
    print("Сотрудники с окладом меньше 20 000 рублей:")
    for value in new_list:
        payment = value.split()
        midle += float(payment[1])
        if float(payment[1]) <= 20000:
            print(payment[0], end=" ")

    print(f"\nСредняя зарплата равна {midle / len(new_list)}")


