import time
class TrafficLight:
    __color1 = "Red"
    __color2 = "Yellow"
    __color3 = "Green"
    def running(self):
        while True:
            print(self.__color1)
            time.sleep(7)
            print(self.__color2)
            time.sleep(2)
            print(self.__color3)
            time.sleep(7)
            print(self.__color2)
            time.sleep(2)
a = TrafficLight()
a.running()


