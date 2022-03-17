list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
new_number = int(input('Введите новый элемент рейтинга в виде целого числа - '))
a = 0

for b in list:
    if new_number <= b:
        a += 1

    elif new_number > b:
        break

list.insert(a, float(new_number))
print (list)