import json
with open("text-json.txt", "w", encoding="UTF-8") as f1:
    with open("text_7.txt", "r", encoding="UTF-8") as f:
        dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        medium = [dict, {"средняя прибыль:": sum([int(i) for i in dict.values() if int(i) > 0]) / len([int(i) for i in dict.values() if int(i) > 0])}]
    json.dump(medium, f1, ensure_ascii=False)
