# Create a car class with a attributes of year_model, make and speed
class Car:
# __init__ method that accepts car's year model and make as an argument
    def __init__(self, year_model, make):
        # private members
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
# accelarate method that add 5 to the speed attributes each time it is called
    def accelerate(self):
        self.__speed += 5
# brake method that subtract 5 to the speed attributes each time it is called
    def brake(self):
        self.__speed -= 5
# get speed method
    def get_speed(self):
        #return the speed attribute
        return self.__speed
    
# Create a car object
car = Car(2012, "Ford")
print("\nThe car is accelerating...\n")
# Call the speed attribute five times
for i in range(5):
    car.accelerate()
    print("The current speed is: ", car.get_speed())