from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, cloth):
        self.cloth = cloth
    @property
    @abstractmethod
    def consumpsion(self):
        pass
    def __add__(self, other):
        return self.consumpsion + other.consumpsion

class Coat(Clothes):
    @property
    def consumpsion(self):
        return self.cloth / 6.5 + 0.5
class Suit(Clothes):
    @property
    def consumpsion(self):
        return self.cloth * 2 + 0.3
a = Coat(20)
b = Suit(10)
print(f"Итоговый расход ткани: {a + b}")

