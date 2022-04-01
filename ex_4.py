rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("ex4a.txt", 'w', encoding='utf-8') as af:
    with open("ex4b.txt", 'r', encoding='utf-8') as bf:
        af.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in bf]))