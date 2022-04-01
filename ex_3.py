with open('ex_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'средняя зарплата = {round(sum(employees_dict.values()) / len(employees_dict), 10)}\n'
          f'сотрудников с зарплатой меньше 20 000 {[e[0] for e in employees_dict.items() if e[1] < 20000]}')