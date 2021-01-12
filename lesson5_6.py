my_dict = {}
with open("text_6.txt", "r", encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(":")
        summa = sum(map(int, "".join([i for i in stats if i == ' ' or "9" >= i >= "0"]).split()))
        my_dict[name] = summa
print(my_dict)
