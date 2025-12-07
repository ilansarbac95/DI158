# Exercice 1 
#Instantiate three Cat objects using the code provided above.
#Outside of the class, create a function that finds the oldest cat and returns the cat.
#Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Instantiate three Cat objects
cat1 = Cat("Chamallow", 2)
cat2 = Cat("Simba", 3)
cat3 = Cat("Fifi", 4)

def find_oldest_cat(cats):
    """Finds the oldest cat from a list of Cat items"""
    if not cats:
        return None  # Return None if the list is empty

    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest = find_oldest_cat([cat1, cat2, cat3])
if oldest:
    print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")
else:
    print("No cats provided")

# Exercice 2 : 
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

# Create davids_dog
davids_dog = Dog("Rex", 50)

# Print davids_dog details and call methods
print(f"David's dog name: {davids_dog.name}")
print(f"David's dog height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

# Create sarahs_dog
sarahs_dog = Dog("Teacup", 20)

# Print sarahs_dog details and call methods
print(f"Sarah's dog name: {sarahs_dog.name}")
print(f"Sarah's dog height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Check which dog is bigger
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is the bigger dog.")
else:
    print("Both dogs are the same height.")

# Exercice 3 : 
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Create an object # I preferred Starman David Bowie ^^ 
starman = Song(["starman waiting in the sky",
                "He'd like to come and meet us",
                "But he thinks he'd blow our minds"])

# Call the sing_me_a_song method
starman.sing_me_a_song()

# Exercice 4 : 

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        sorted_animals = {}
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = [animal]
            else:
                sorted_animals[first_letter].append(animal)
        return sorted_animals

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            if len(animals) == 1:
                print(f"{letter}: {animals[0]}")
            else:
                print(f"{letter}: {animals}")

# Create an object
new_york_zoo = Zoo("New York Zoo")

# Add animals
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Lion")
new_york_zoo.add_animal("Elephant")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Ape")

# Get animals
new_york_zoo.get_animals()

# Sell an animal
new_york_zoo.sell_animal("Lion")

# Get animals after selling
new_york_zoo.get_animals()

# Get animal groups
new_york_zoo.get_groups()
