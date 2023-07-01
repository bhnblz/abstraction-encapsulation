class PetInterface:
    def name(self):
        name = input("\n\033[31mEnter pet's name: ")
        return name
    def animal_type(self):
        animal_type = input("\033[32mEnter the animal type: ")
        return animal_type
    def age(self):
        age = input("\033[33mEnter the age of the pet: ")
        return age