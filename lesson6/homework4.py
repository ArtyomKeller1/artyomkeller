from random import randint
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        print(f"Машина повернула {direction}")
class TownCar(Car):
    def show_speed(self):
        a = randint(1, 100)
        if a > 60:
            print(f"Автомобиль превысил скорость({a})")
        else:
            print(f"Скорость автомобиля {a}")
class WorkCar(Car):
    def show_speed(self):
        a = randint(1, 100)
        if a > 40:
            print(f"Автомобиль превысил скорость({a})")
        else:
            print(f"Скорость автомобиля {a}")
class SportCar(Car):
    def show_speed(self):
        a = randint(1, 150)
        print(f"Скорость автомобиля {a}")
class PoliceCar(Car):
    def show_speed(self):
        a = randint(1, 150)
        print(f"Скорость автомобиля {a}")
Car.go(Car)
Car.stop(Car)
Car.turn(Car, "влево")
WorkCar.show_speed(WorkCar)
TownCar.show_speed(TownCar)
PoliceCar.show_speed(PoliceCar)
SportCar.show_speed(SportCar)


