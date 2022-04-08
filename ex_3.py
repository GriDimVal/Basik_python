class Worker:
    def __init__(self, name, surename, position, zarplata, bonus):
        self.name = name
        self.surename = surename
        self.position = position
        self._dohod = {'ZP': zarplata, "premiya": bonus}

class Position (Worker):
    def get_full_name(self):
        return f"{self.name} {self.surename}"

    def get_full_position(self):
        return f"{sum(self._dohod.values())}"

people = Position("Ivan", "Ivanovich", "GenDir", 1000, 500)

print(people.get_full_name())
print(people.position)
print(people.get_full_position())