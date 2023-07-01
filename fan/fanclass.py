# Create a class named Fan
class Fan:
# Input three constant named SLOW, MEDIUM, AND FAST with a values of 1,2, and 3to denote the speed of the fan
    SLOW = 1
    MEDIUM = 2
    FAST = 3
# constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        # Private int data field named speed
        self.__speed = speed
        # Private float data field named radius that specifies the radius of the fan
        self.__radius = radius
        # Private string data field named color that specifies the color of the fan
        self.__color = color
        # Private bool data field named on that specifies the speed of the fan
        self.__on = on
    # Get speed
    def get_speed(self):
        return self.__speed
    # Set speed
    def set_speed(self, speed):
        self.__speed = speed
    # whether the fan is on or off
    def fan_is_on(self):
        return self.__on  
    # Set on
    def set_on(self, on):
        self.__on = on
    # Get radius
    def get_radius(self):
        return self.__radius
    # Set radius
    def set_radius(self, radius):
        self.__radius = radius
    # Get color
    def get_color(self):
        return self.__color
    # Set color
    def set_color(self, color):
        self.__color = color