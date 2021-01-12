from sys import argv
script_name, work_hours, pay_hour, bonus = argv
print('Имя скрипта', script_name)
print('Часы работы', work_hours)
print('Ставка в час', pay_hour)
print('Премия', bonus)
def pay():
    try:
        payment = int(work_hours) * int(pay_hour) + int(bonus)
        print("Зарплата за месяц составит: ", payment)
    except ValueError:
        print("Вводите только целые числа")
(pay())



