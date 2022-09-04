# multiple inheritance

# inherit from multiple class at the same time

# Vehicle Class

class Vehicle:
    speed = 0

    def drive(self, speed):
        self.speed = speed
        print('Driving')

    def stop(self, speed):
        self.speed = 0
        print('Stopped')

    def display(self):
        print(f'Driving at {self.speed} speed')


# Freezer Class
class Freezer:
    temp = 0

    def freeze(self, temp):
        self.temp = temp
        print('Freezing')

    def display(self):
        print(f'Freezing at {self.temp} temp')


'''
case 1 :

class FreezerTruck( Freezer, Vehicle):
    def display(self):
        pass


'''

'''
case 2 :

class FreezerTruck(Vehicle, Freezer):
    def display(self):
        pass


'''


class FreezerTruck(Vehicle, Freezer):  # here we define the Method Resolution Order (MRO)
    def display(self):
        print(f'Is a freezer: {issubclass(FreezerTruck,Freezer)}')
        print(f'Is a vehicle: {issubclass(FreezerTruck,Vehicle)}')

        # super(Freezer, self).display()  # Fails because MRO
        # super(Vehicle, self).display() # works because MRO

        Freezer.display(self)  # works
        Vehicle.display(self)  # works


t = FreezerTruck()

t.drive(50)
t.freeze(-30)
print('-'*20)

# both class has display method
t.display()


'''
case 1:

    class FreezerTruck(Freezer, Vehicle):
    pass
    
output > 

Driving
Freezing
--------------------
Freezing at -30 temp

case 2:

    class FreezerTruck(Vehicle, Freezer):
    pass
    
output > 

Driving
Freezing
--------------------
Driving at 50 speed

takeout: first come first serve >  (MRO) rule

'''
