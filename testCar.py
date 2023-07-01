# Import Car class
from CarClass import Car

# Create an car object
car = Car(2012, "Ford")

print("Accelerating....")
for i in range(5):
    car.accelerate()
    print("The current speed is :", car.get_speed())