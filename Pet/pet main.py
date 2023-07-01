#Import the interface files (PetClass and pestInterface) to the main file(pet main.py)
from PetClass import Pet
from petinterface import PetInterface

# Create objects
pet = Pet()
pi = PetInterface()

# Ask the user for the pet's name, type, and age
pet.set_name(pi.name())
pet.set_animal_type(pi.animal_type())
pet.set_age(pi.age())

# Display the pet's name, type, and age
print("\nPet's Name: ", pet.get_name())
print("Animal Type: ", pet.get_animal_type())
print("Pet's Age: ", pet.get_age())