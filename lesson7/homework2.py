class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h
    @property
    def coat(self):
        return self.v/6.5 + 0.5
    @property
    def suit(self):
        return 2*self.h + 0.3
c = Clothes(1, 2)
print(c.coat)
print(c.suit)


