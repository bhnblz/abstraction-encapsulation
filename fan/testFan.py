# Import fanclass to the main file (testFan)
from fanclass import Fan
# Create test fan class
class TestFan:
    def main(self):
        # Fan 1 objects
        fan1 = Fan(Fan.FAST, 10, 'yellow', True)

        print("Fan 1 Properties: ")
        print("Speed:", fan1.get_speed())
        print("Radius:", fan1.get_radius())
        print("Color:", fan1.get_color())
        print("On [on = True, off = False]:", fan1.fan_is_on())
    

# Create Instance of the TestFan to run
test_fan = TestFan()
test_fan.main()