def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    yield factorial
for el in fact(6):
    print(el)