#Exercise 1 : Favorite Numbers

my_fav_numbers = {1, 5, 7, 9, 15, 19}
print("My favorite numbers:", my_fav_numbers)

while True:
    try:
        user_input = input("Add a number to my_fav_numbers (or 'stop' to finish): ")
        if user_input.lower() == "stop":
            break
        number_to_add = int(user_input)
        if number_to_add not in my_fav_numbers:
            my_fav_numbers.add(number_to_add)
            print(f"{number_to_add} has been added to my_fav_numbers")
        else:
            print(f"{number_to_add} is already in my_fav_numbers.")
    except ValueError:
        print("Please enter a number or 'stop'.")

print("my_fav_numbers updated:", my_fav_numbers)

number_to_delete = int(input("Which number to delete from my_fav_numbers? "))
if number_to_delete in my_fav_numbers:
    my_fav_numbers.remove(number_to_delete)
    print(f"{number_to_delete} has been deleted from my_fav_numbers")
else:
    print(f"{number_to_delete} is not in my_fav_numbers.")

print("my_fav_numbers final:", my_fav_numbers)

friend_fav_numbers = {3, 6, 9, 12, 15} 
print("Friend's favorite numbers:", friend_fav_numbers)

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print("Our favorite numbers:", our_fav_numbers)


#Exercise 2 :

#No it is not possible to add integers to the tuple because a tuple is immuable and 
# if i add an element an error will pop-up. 


#Exercise 3 :

basket = ["Banana", "Apples", "Oranges", "Blueberries"] 
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)

apple_count = basket.count("Apples")
print(f"There are {apple_count} Apples in the basket")

basket.clear()
print("Basket is empty as you can see", basket)

#Exercice 4 : 
#Un Float est la représentation de nombres décimaux tandis qu'un Integer 
# sont des nombres entiers.

#Exemples de floats : 
my_list = []
start = 1.5

while start <= 5:
    my_list.append(start)
    start += 0.5

print(my_list)

#Une autre méthode consiste l'utilisation de range():
my_list = [i / 2.0 + 1 for i in range(3, 11)]
print(my_list)

#Exercice 5 
for number in range(1, 21): 
    print(number)

# --> et pour uniquement un index pair: 
for index in range(1, 21):
    if index % 2 == 0:  
        print(index)

#Exerice 6 :
my_name = "Ilan"

while True:
    user_name = input("What is your Name: ")
    if user_name == my_name:
        print("Hello, it is me !")
        break  
    else:
        print("It is not me. Please retry.")

#Exerice 7 : 
favorite_fruits = input("list your favorite fruits (separated with a space) : ").split()
fruit_choice = input("Enter the name of a fruit: ")

if fruit_choice in favorite_fruits:
    print("You chose one of your favorite fruits")
else:
    print("You chose a new fruit.")


#Exercice 8:
toppings = []
total_price = 10.0  # Base price of the pizza

while True:
    topping = input("Put your ingredient to make your Pizza (or 'quit' to finish) : ")
    if topping.lower() == 'quit':
        break  
    else:
        toppings.append(topping)
        total_price += 2.5
        print(f"You added {topping} for your Pizza")

print("\nHere are your ingredients for your Pizza :")
for topping in toppings:
    print(f"- {topping}")

print(f"\nThe total price for your pizza : {total_price} shekels.")


#Exercice 9 : 
total_cost = 0

while True:
    try:
        age = int(input("Enter the Age of the person (or 'stop' to finish) : "))
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        total_cost += ticket_price
        print(f"Tcket price : ${ticket_price}")
    except ValueError:
        user_input = input("Do you want to add other persons ? (yes/no) ").lower()
        if user_input != "yes":
            break

print(f"The total price of the tickets is : ${total_cost}")


#Exercice 10 : 

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []

# To delete all "Pastrami sandwich"
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# To prepare Sandwich and moving them to finished_sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich}")

print("\nPrepared Sandwiches :")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")