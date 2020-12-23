class Stationary:
    def __init__(self, title, draw):
        self.title = title
        self.draw = draw
    def draw(self, title):
        print(f"Запуск отрисовки {title}")
class Pen(Stationary):
    a = __qualname__
    def draw(self, title):
        super().draw(self, title)
class Pencil(Stationary):
    b = __qualname__
    def draw(self, title):
        super().draw(self, title)
class Handle(Stationary):
    c = __qualname__
    def draw(self, title):
        super().draw(self, title)
Pen.draw(Pen, "Карандаш")
Pencil.draw(Pencil, "Ручка")
Handle.draw(Handle, "Маркер")