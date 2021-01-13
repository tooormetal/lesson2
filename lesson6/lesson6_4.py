class Car:
    speed = "скорость"
    color = "цвет"
    name = "название"
    is_police = "True or False"
    def go(self):
        print("машина поехала")
    def stop(self):
        print("машина остановилась")
    def turn(self):
        print("машина повернула")
    def show_speed(self):
        print(f"текущая скорость {speed}")
class TownCar(Car):
    speed = 60
    color = "red"
    name = "lincoln"
    is_police = False
    def show_speed(self):
        if int(self.speed) > 60:
            print(f"разрешенная скорость 60, вы превышаете!")
class SportCar(Car):
    speed = 180
    color = "blue"
    name = "ferrari"
    is_police = False
class WorkCar(Car):
    speed = 80
    color = "yellow"
    name = "bobcat"
    is_police = False
    def show_speed(self):
        if int(self.speed) > 60:
            print(f"разрешенная скорость 60, вы превышаете!")
class PoliceCar(Car):
    speed = 40
    color = "black"
    name = "Lada"
    is_police = True
b = WorkCar()
b.show_speed()


