# pet_dog.py
import random
from dog import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *other_dogs):
        dog_names = [self.name] + [dog.name for dog in other_dogs]
        print(f"{', '.join(dog_names)} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained.")

# Test the PetDog class
dog1 = PetDog("Buddy", 5, 20)
dog2 = PetDog("Max", 3, 15)
dog3 = PetDog("Rocky", 4, 18)

dog1.train()
dog1.play(dog2, dog3)
dog1.do_a_trick()
dog2.do_a_trick()