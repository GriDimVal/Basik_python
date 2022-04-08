class Stationary:
    def __init__(self, title='может рисовать'):
        self.title = title

    def draw(self):
        print(f'начнем рисовать {self.title}')

class Pen(Stationary):
    def draw(self):
        print(f'начнем рисовать {self.title} ручкой')

class Pencil(Stationary):
    def draw(self):
        print(f'начнем рисовать {self.title} карандашом')

class Marker(Stationary):
    def draw(self):
        print(f'начнем рисовать {self.title}')

stat = Stationary()
pen = Pen("Крутой")
pencil = Pencil("Простым")

office_starts = [stat,pen, pencil]

for i in office_starts:
    i.draw()