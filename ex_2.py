# вводим новый класс - дорога с параметрами длины и ширины
class Road:
    def __init__(self, lenght, weidth, lines):
       self._lenght = lenght
       self._weidht = weidth
       self._lines = lines
#пишем функцию по расчету необходимой массы асфальта
    def get_full_proffit(self):
        return f"{self._lenght} метров * {self._weidht} метров * {self._lines} полосы * 25 киллограмов * 5 сантиметров = {(self._lenght * self._weidht * self._lines * 25 * 5) / 1000} тонн"
#вводим параметры дороги, длиной 5 километров, шириной 5 метров по 4 полосы
road_1 = Road(5000,5, 4)
print(road_1.get_full_proffit())