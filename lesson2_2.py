el = list(input("Введите элементs списка списка: ").split())
for i in range(1, len(el), 2):
    el[i - 1], el[i] = el[i], el[i - 1]
print(el)


