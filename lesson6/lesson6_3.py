class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")
    def get_total_income(self):
        print(f"{sum(self._income.values())}")
a = Position("Павел", "Андрацкий", "менеджер", 5000, 7000)
print(a.surname)
a.get_full_name()
a.get_total_income()



