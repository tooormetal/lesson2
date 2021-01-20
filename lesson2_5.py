reiting = [8, 6, 4, 2, 1]
new = int(input('Введите новое число: '))
number = 0
for i in reiting:
    if new <= i:
        number += 1
reiting.insert(number, new)
print(reiting)
