from colorama import Fore
# Import Car class
from CarClass import Car

# Create an car object
car = Car(2012, "Ford")
print(Fore.BLUE, "\nAccelerating....\n")
# Calling accelerate method 5 times
for i in range(5):
    car.accelerate()
    print(Fore.LIGHTCYAN_EX, "The current speed is :", car.get_speed())

print(Fore.BLUE, "\nBraking....\n")
# Calling brake method five times
for i in range(5):
    car.brake()
    print(Fore.LIGHTCYAN_EX, "The current speed is: ", car.get_speed())