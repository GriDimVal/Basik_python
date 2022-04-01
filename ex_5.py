from functools import reduce

def new_list (a_1, a_2):
    return a_1 + a_2

list = [a for a in range (100, 1001, 2)]
print(f"Лист\n{list}\nсумма четных чисел\n{reduce(new_list, list)}")