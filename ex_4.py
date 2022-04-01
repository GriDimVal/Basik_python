from random import randint

my_list = [randint(-20, 20) for _ in range (20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Исходный лист\n{my_list}\nдублирует лист\n{new_list}')