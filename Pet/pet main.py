from PetClass import Pet
from petinterface import PetInterface

pet = Pet()
pi = PetInterface()

pet.set_name(pi.name())
print("Pet's Name: ", pet.get_name())