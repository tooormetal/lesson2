
def my_sum():
    summ = 0
    while True:
        print("Для выхода нажмите 'E'")
        my_list = input("введите числа через пробелы: ").split()
        for i in my_list:
            if i == 'E':
                return summ
            else:
                try:
                    summ += int(i)
                except ValueError:
                    print("вводите только числа, для выхода 'E'")
        print(f'Сумма равна: {summ}')
print(my_sum())