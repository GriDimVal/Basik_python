def convert (sec):
    sec = sec%(24*3600)
    hour= sec // 3600
    sec %= 3600
    min = sec// 60
    sec %= 60
    print ('часов в секундах', hour)
    print ('минут в секундах', min)
    return '%02d:%02d:%02d' % (hour,min,sec)

a=int(input ('Введите число от 0 до 86 399 (без пробелов)'))
print('время составляет', convert (a))