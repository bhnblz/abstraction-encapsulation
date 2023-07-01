# Import fanclass to the main file (testFan)
from fanclass import Fan
# Create test fan class
class TestFan:
    def fan(self):
        # Fan 1 object
        fan_1 = Fan(Fan.FAST, 10, "yellow", on=True)

        print("\n\033[31mFAN 1 PROPERTIES: ")
        print("\033[35mSpeed:", fan_1.get_speed())
        print("\033[34mRadius:", fan_1.get_radius())
        print("\033[33mColor:", fan_1.get_color())
        print("\033[32mOn [on = True, off = False]:", fan_1.fan_is_on())
    
        # Fan 2 object
        fan_2 = Fan(Fan.MEDIUM, 5, "blue", on=False)

        print("\n\033[31mFAN 2 PROPERTIES: ")
        print("\033[32mSpeed:", fan_2.get_speed())
        print("\033[33mRadius:", fan_2.get_radius())
        print("\033[34mColor:", fan_2.get_color())
        print("\033[35mOn [on = True, off = False]:", fan_2.fan_is_on())
    
# Create Instance of the TestFan to run
test_fan = TestFan()
test_fan.fan()