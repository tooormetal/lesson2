from random import randint

with open("lesson5.txt", "w", encoding="utf-8") as f:
    my_list = [randint(1, 100) for i in range(100)]
    f.write(" ".join(map(str, my_list)))
print(f"сумма элементов равна {sum(my_list)}")
