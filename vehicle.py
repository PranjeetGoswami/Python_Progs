class Vehicle:
    def start_engine(self):
        print("Starting the vehicle's engine...")
        
class Car(Vehicle):
    def start_engine(self):
        print("Starting the car's engine...")
        
class Motorbike(Vehicle):
    def start_engine(self):
        print("Starting the motorbike's engine...")
        
vehicle = Vehicle()
vehicle.start_engine()

car = Car()
car.start_engine()

motorbike = Motorbike()
motorbike.start_engine()
