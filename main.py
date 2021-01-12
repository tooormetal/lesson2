with open("text_3.txt", "r", encoding="utf-8") as pay:
    new_list = pay.readlines()
    midle = 0
    for value in new_list:
        payment = value.split()
        midle += float(payment[1])
    print(f"Средняя зарплата равна {midle / len(new_list)}")
