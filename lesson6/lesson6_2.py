class Road:
    def mass(self, __length, __width):
        print(f"Масса асфальта длиной {__length} и шириной {__width} равна {round(__length * __width * 25 * 5 / 1000)} тонн")
a = Road()
a.mass(5000, 20)