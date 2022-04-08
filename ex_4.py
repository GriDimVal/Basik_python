#создаем базовый класс автомобиль
class Car:
    #вводим конструктор параметров
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Тип машины {self.name} (Цвет {self.color}) машина полицейская - {self.is_police}")
# Вводим варианты действий машины
    def go(self):
        print(f"{self.name}: машина в движении")
    def stop(self):
        print(f"{self.name}: машина остановилась")
    def turn(self, direction):
        print(f"{self.name}: машина поворачивает {'на лево' if direction == 0 else 'на право'}")
    def show_speed(self):
        print(f"{self.name}: скорость машины - {self.speed}")

class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}: скорость автомобиля - {self.speed} - скорость превышена!" \
            if self.speed > 40 else f"скорость автомобиля - {self.speed}"
class TownCar(Car):
    def show_speed(self):
        return f"{self.name}: скорость автомобиля - {self.speed} - скорость превышена!" \
            if self.speed > 40 else f"скорость автомобиля - {self.speed}"
class SportCAR(Car):
    def show_speed(self):
        return f"{self.name}: скорость автомобиля - {self.speed} - скорость превышена!" \
            if self.speed > 100 else f"скорость автомобиля - {self.speed}"
class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar("Полицейская с мигалкой", "Белый в синюю полоску", 90)
police_car.go()
police_car.show_speed()
police_car.turn(2)

print("*" * 70)

work_car = WorkCar("Toyota", "Красный", 70)
work_car.go()
work_car.turn(0)

print("*" * 70)

town_car = TownCar("Ford", "Белый", 30)
town_car.go()
town_car.turn(10)