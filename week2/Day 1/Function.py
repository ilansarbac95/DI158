from functools import reduce

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# Filtrer les noms de 4 lettres ou moins
filtered_people = filter(lambda name: len(name) <= 4, people)

# Dire bonjour à chaque personne filtrée
greeted_people = map(lambda name: "Hello " + name + "!", filtered_people)

# Afficher le résultat
print(list(greeted_people))

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered_people = filter(lambda name: len(name) <=4, people)
greeted_people = map(lambda name: "Hello" + name + "!", filtered_people)
print(list(greeted_people))