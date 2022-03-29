def personal_inf(**kwargs):
    return ' '.join(kwargs.values())


params = {
    'name': input('Введите имя - '),
    'surname': input('Введите фамилию - '),
    'birthday': input('Введите дату рождения - '),
    'adress': input('введите город проживания - '),
    'e-mail': input('введите адресс электронной почты - '),
    'phone': input('введите номер контактного телефона - '),
}

print(personal_inf(**params))