goods = []
features = {'Название': '', 'цена': '', 'количество': '', 'Единицы измерения': ''}
analytics = {'Название': [], 'цена': [], 'количество': [], 'Единицы измерения': []}
num = 0

while True:
    if input('Для выхода из приложения назмите Q, для продолжения нажмите "enter": ').upper() == 'Q':
        break
    num +=1
    for f in features.keys():
        prop = input(f'Введите данные для {f} - ')
        features[f] = int(prop) if f in ('цена', 'rjkbxtcndj') else prop
        analytics[f].append(features[f])
goods.append((num, features.copy()))
print(f"\nструктура товаров\n{goods}")
print(f"\nАналитика по товарам\n{'*' * 30}")
for key, value in analytics.items():
    print(f"{key[:25]:>30}: {value}")
print("*" * 30)
