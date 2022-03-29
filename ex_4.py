def my_new_function (x,y):
    try:
        x, y = float (x), int (y)
        if x <= 0 or y >= 0:
            return 'Ошибка задачи: "X" должен быть больше "0", а "Y" должен быть меньше "0"'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1/x
            return f'резудьтат возыведения х в степень у: {round(result, 15)}'
    except ValueError:
        return 'Программа работает только с числами.'

print(my_new_function(2, -8))