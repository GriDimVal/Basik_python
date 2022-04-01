# в созданный (самостоятельно, не програмно) файл вносим различные строки, как только нажмем
# 'Enter' (на пустом значении) программа останавливается
with open('ex_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('введите новую строку - ')
        if not line:
            break
        f.write(f'{line}\n')