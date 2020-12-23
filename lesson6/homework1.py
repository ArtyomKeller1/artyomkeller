from time import sleep
class TrafficLight:
    def __init__(self, __color):
        self.__color = __color
        __color = "красный"
        print("Красный")
        sleep(7)
        __color = "зелёный"
        print("Жёлтый")
        sleep(2)
        __color = "зелёный"
        print("Зелёный")
        sleep(8)

TrafficLight("красный")