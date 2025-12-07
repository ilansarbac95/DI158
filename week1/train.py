

my_list = []
start = 1.5

while start <= 5:
    my_list.append(start)
    start += 0.5

print(my_list)

#Une autre méthode consiste l'utilisation de range() 
my_list = [i / 2.0 + 1 for i in range(3, 11)]
print(my_list)

#Exercice 5 
