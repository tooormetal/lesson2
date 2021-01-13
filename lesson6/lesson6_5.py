class Stationery:
    title = "название"
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    title = "ручка"
    def draw(self):
        print("Запуск отрисовки ручкой")
class Pencil(Stationery):
    title = "карандаш"
    def draw(self):
        print("Запуск отрисовки карандашем")
class Handle(Stationery):
    title = "маркер"
    def draw(self):
        print("Запуск отрисовки маркером")
a = Handle()
a.draw()