# Import Car class
from CarClass import Car

# Create an car object
car = Car(2012, "Ford")
print("\nAccelerating....\n")
# Calling accelerate method 5 times
for i in range(5):
    car.accelerate()
    print("The current speed is :", car.get_speed())

print("\nBraking....\n")
# Calling brake method five times
for i in range(5):
    car.brake()
    print("The current speed is: ", car.get_speed())