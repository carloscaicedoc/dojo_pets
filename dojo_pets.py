class Pet:

    def __init__(self, name, types, tricks):
        self.name = name
        self.types = types
        self.tricks = tricks
        self.energy = 75
        self.health = 75

    def sleep( self ):
        self.energy += 25
        return self

    def eat( self ):
        self.energy += 5
        self.health += 10
        return self

    def play( self ):
        self.health += 5
        self.energy -= 10
        return self

    def noise( self ):
        print("BOUGH-WOUGH AOUUU AOUUU")
        print("-----------------------")

    def dog_information ( self ):
        print( f"{self.name}: {self.types} & {self.tricks}" )
        return self

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed( self ):
        self.pet.eat()
        return self
    
    def bathe( self ):
        self.pet.noise()
        return self
    
    def print_info ( self ):
        print( f"Owner: {self.first_name} {self.last_name}, Pet Name: {self.pet.name}, Treats: {self.treats}, Pet Food: {self.pet_food}.")
        print( f"Pet's Energy: {self.pet.energy}, Pet's Health: {self.pet.energy}")
        self.pet.dog_information()


pet1 = Pet("Valentina", "Siberian Husky", "Dog athlete")
elena = Ninja("Elena", "Ishikawa", "Bone", "Raw dog food", pet1)
# elena.print_info()

henry= Ninja("Henry", "Kubric", "Fruit", "Corn", Pet("Taco", "Parrot", "Singer"))
# henry.print_info()

pet3 = Pet("Mango", "Goat", "Comedian")
charles = Ninja("Charles", "Wolf", "Rye Bread", "Leftovers", pet3)
# charles.print_info()

# charles.print_info()
charles.feed()
# charles.print_info()
charles.walk()
# charles.print_info()
charles.walk()
charles.print_info()

elena.feed()
elena.walk()
elena.feed()
elena.print_info()

henry.feed()
henry.feed()
henry.walk()
henry.feed()
henry.print_info()