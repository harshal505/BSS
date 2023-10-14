class End_ate:
    a = 10
    _b = 20
    __c = 50


obj = End_ate()
print(obj.a)


class Beta(End_ate):

    def __init__(self):
        print(self._b)


obj1 = Beta()
