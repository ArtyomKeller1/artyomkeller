class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def calc(self, lenght, width, mass, thickness):
        print(lenght*width*mass*thickness)

Road.calc("Дорога 1",2,3,4,5)