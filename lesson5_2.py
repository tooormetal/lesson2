with open("text.txt", "r", encoding="utf-8") as moon:
    my_list = moon.readlines()
    print(f"количество строк равно {len(my_list)}")
    for index, value in enumerate(my_list, 1):
        word = len(value.split())
        print(f" количество слов в строке {index} равно {word}")

