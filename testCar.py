# Import Car class
from CarClass import Car

# Create an car object
car = Car(2012, "Ford")
# Calling accelerate method 5 times
print("Accelerating....")
for i in range(5):
    car.accelerate()
    print("The current speed is :", car.get_speed())