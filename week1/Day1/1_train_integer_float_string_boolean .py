#integer
age = 21
players = 3
year = 1989
print (age)
print(players)
print (year)

#float
note = 13.5
distance = 3.5
price = 19.99

print (f"tu as une note de {note} sur 20")
print (f"La distance que tu as parcouru est de {3.5} km/h")
print (f"Le prix de la Bande Dessinée est de {price} euros")

#string
planete = "Mars"

print (f"Nous irons bientôt coloniser la planète {planete} avec une note que je qualifierai de {distance} à peu près.")

#boolean
running = True
print (f"the game is running: {running}")

if running: 
    print("The game is running")
else: 
    print("The game is over")

online = False
print (f"Are you online? {online}")

if online:
    print("Your are online")
else:
    print("you are offline")

i,n,f,p = "introverted", "intuition", "feeling", "perception"
print (f"your mbti is {i}, {n}, {f}, {p}")

e,n,f,j = "extroverted", "intuition", "feeling", "judgement"
print (f"your mbti is {e}, {n}, {f}, {j}")

i = n = f = e = j = p = "Diplomat"
print (f"You belong to {i}")
