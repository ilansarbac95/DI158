class Animal:
    def __init__(self, name, num_legs, sound):
        self.name = name
        self.num_legs = num_legs
        self.sound = sound
    
    def make_sound(self):
        print(f"I go {self.sound}")

class Dog(Animal):
    def fetch(self):
        print("Iam a dog and I go fetch sticks")

prince = Dog('Prince', 4, 'Waf')
prince.make_sound()

tippy = Dog('Tippy', 3, 'Woof')
tippy.make_sound()
tippy.fetch()

print(tippy.num_legs)

ralph = Animal('Ralph', 2, 'squak')
ralph.make_sound()


        