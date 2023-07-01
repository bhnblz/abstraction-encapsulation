from PetClass import Pet
from petinterface import PetInterface

pet = Pet()
pi = PetInterface()

pet.set_name(pi.name())
print("Pet's Name: ", pet.get_name())

pet.set_animal_type(pi.animal_type())
print("Animal Type: ", pet.get_animal_type())