def my_func(x, y):
    result = 1
    if x > 0 and y < 0:
        for i in range(abs(y)):
            result = result / x
    else:
        result = "error!"
    print(result)
my_func(4, -3)
