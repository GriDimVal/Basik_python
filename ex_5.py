def num_sum():
    a = 0
    while True:
        in_list = input('Введите число (через пробел) или Q для выхода: ').split()
        for num in in_list:
            if num == 'Q':
                return a
            else:
                try:
                    a += int(num)
                except ValueError:
                    print('что бы выйти из программы нажмите q - ')
        print(f'сумма чисел = {a}')

print(num_sum())