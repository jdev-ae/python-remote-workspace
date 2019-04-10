class Bike:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __repr__(self):
        return str(self.kwargs)


bk = Bike(load=12, wheels=12)
print(str(bk))
