from googletrans import Translator
with open("text_4.txt_new", "w", encoding="utf-8") as t:
    with open("text_4.txt", "r", encoding="utf-8") as t1:
        text = t1.read()
        t1.write(Translator().translate(text, dest='ru').text)


