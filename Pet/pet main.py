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
print("\n\033[36mGenerating...")
print("\033[31mPet's Name: ", pet.get_name())
print("\033[32mAnimal Type: ", pet.get_animal_type())
print("\033[33mPet's Age: ", pet.get_age())