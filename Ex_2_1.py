from abc import ABC, abstractmethod

class Clothnes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod

    def raschet(self):
        pass

    def __add__(self, other):
        return self.raschet + other.raschet

class Coat(Clothnes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('Маленький размер, пошив начинается с 40 размера.')
        elif size > 58:
            print('Размеры формата "супер большой" шьют в другом магазине, у нас все до 58')
            self.__size = 58
        else:
            self.__size = size

        @property
        def raschet(self):
            return self.__size /6.5 + 0.5

class Costume(Clothnes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('детский размер, не работаем')
            self.__height = 150
        elif height > 250:
            print('огромный размер, ткани не хватит')
            self.__height = 250
        else:
            self.__height = height
    @property
    def raschet(self):
        return 2 * (self.__height / 100) + 0.3

coat_1 = Coat(int(input('введите размер пальто')))
print(f'вам потребуется {coat_1.raschet:.2f} метров ткани на пальто {coat_1.size} размера')
costume_1 = Costume(int(input('введите рост для костюма в сантиметрах')))
print(f'Вам потребуется {costume_1.raschet:.2f} метров ткани на костюм {costume_1.height} роста')
print(f'Вам потребуется всего {coat_1 + costume_1:.2f} метров ткани')