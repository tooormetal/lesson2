def int_funk(text):
    text = input("Введите слова английскими буквами: ").split()
    for word in text:
        chars = 0
        for char in word:
            if ord(char) >= 97 and ord(char) <= 122:
                chars += 1
        if chars == len(word):
            print(word.title())
