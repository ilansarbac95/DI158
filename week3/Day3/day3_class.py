class israeli:
    prime_minister = "Bibi"
    num_citizens = 0

    def __init__(self, name):
        self.name = name
        israeli.num_citizens += 1
        self.__tz = israeli.num_citizens

    def get_tz(self):
        return f"{self.__tz} ?"

liudmila = israeli("liudmila")
gabby = israeli("gabby")
hadriel = israeli("hadriel")
ilan = israeli("ilan")
other_ilan = israeli("other_ilan")
daniel = israeli("daniel")

print(daniel.get_tz)


class MyClass:
  def __init__(self, first_name, last_name):
     self
  @classmethod
  def add(cls,a): 
    return cls.__counter + a

my_class_add = MyClass.add(3)
print(my_class_add)
# >> 3

new_class = MyClass()
new_class.__counter = 1

print(new_class.add(3))
# >> 3


class Person:
    used_names = set()

    def __init__(self, name, age):
        while name in Person.used_names:
            name = input(f"That name '{name}' is taken. Enter another name: ")

        self.name = name
        self.age = age
        Person.used_names.add(name)

    @classmethod
    def fromYear(cls, name, birth_year):
        THIS_YEAR = 2020
        return cls(name, THIS_YEAR - birth_year)

    @property
    def professional_name(self):
        return "Mr " + self.name

# Instances outside the class definition
sharon = Person("Sharon", 29)
markus = Person("Markus", 40)

# Correct call to fromYear
sharone = Person.fromYear('Sharone', 1996)

print(sharon.name)
print(markus.name)
print(sharone.name)
print(sharone.age)
print(sharon.professional_name)