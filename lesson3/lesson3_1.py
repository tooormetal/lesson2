a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))
def my_funk(a, b):
    try:
        return int(a / b)
    except ZeroDivisionError:
        print("Error")

print(my_funk(a, b))
