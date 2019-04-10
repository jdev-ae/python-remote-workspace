class Vehicle():
    
    '''
    Parent for all vehicles
    '''

    saftey_check = 1

    def __init__(self, name, manufacturer, vtype, wheels, color, fuel, tank_size, hp):
        self.name = name
        self.manufacturer = manufacturer
        self.wheels = wheels
        self.type = vtype
        self.color = color
        self.fuel = fuel
        self.tank_size = tank_size
        self.hp = hp
        saftey_check = 2


vehicle1 = Vehicle(name='i20', manufacturer='Hundai', vtype='car', wheels=4, color='black', fuel='diesel', tank_size='20 gal', hp=600)
vehicle2 = Vehicle(name='i20', manufacturer='Hundai', vtype='car', wheels=4, color='black', fuel='diesel', tank_size='20 gal', hp=600)

print(vehicle1.saftey_check)
# vehicle1.saftey_check = False
print(vehicle2.saftey_check)
# print(vehicle1.saftey_check)
