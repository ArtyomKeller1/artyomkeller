class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 100, "bonus": 200}
class Position(Worker):
    def get_full_name(self, name, surname):
        return name, surname
    def get_total_income(self, _income):
        a = _income.get("wage")
        b = _income.get("bonus")
        return a+b

print(Position.get_full_name(Worker, "Григорий", "Петров"))
print(Position.get_total_income(Position, _income={"wage": 100, "bonus": 200}))
