#Exercise 1 : 
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
combined_pairs = zip(keys, values)
result = dict(combined_pairs)
print(result)

#Exercice 2 : 
family = {}
total_cost = 0

while True:
    name = input("Entrez le nom de la personne (ou 'stop' pour terminer) : ")
    if name.lower() == 'stop':
        break
    try:
        age = int(input("Entrez l'âge de la personne : "))
        family[name] = age  # Ajoute le nom et l'âge au dictionnaire

        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15

        total_cost += ticket_price
        print(f"{name.capitalize()} has to pay ${ticket_price}.")

    except ValueError:
        print("Veuillez entrer un âge valide.")

print(f"\nThe family's total cost is ${total_cost}.")
    