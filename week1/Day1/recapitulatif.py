print(type(42))
print(type(42.5))

b = 3.5
print(type(b))
print(type("helloworld"))

print("helloworld".capitalize())
print("HELLOWORLD".lower())

print("goodnight moon")
print("goodnight moon".replace("goodnight", "hello"))

print("Hello world\nMy name is Rick\nHow are you doing today?")


try: # le try permet de relever les erreurs potentiels et qu'il faut toujours placer au tout début
    age = int(input("Entrez votre âge : "))
    is_adult = age >= 18
    print(is_adult)

    if is_adult:
        print("Vous êtes un adulte.")
    else:
        print("Vous êtes mineur.")
except ValueError:
    print("Veuillez entrer un âge valide (nombre entier).")



# autre cas de figure
try:
    num1 = int(input("Entrez le premier nombre : "))
    num2 = int(input("Entrez le deuxième nombre : "))
    sum = num1 + num2
    print(f"La somme est : {sum}")
except ValueError:
    print("Veuillez entrer des nombres entiers valides.")

#list 
my_name = "Jack"
hello = "Hello World"
my_age = 27
my_list = [my_name, my_age, hello]

#tuple (qui utilise des parenthèses et ne peuvent changer)
my_tuple = (1+3, 2.7, 'Thursday')

#string 
my_string = "I love cheese!"

#Indexing a sequence : 
my_name = "Jack"
hello = "Hello World"
my_age = 27

my_list = [my_name, hello, my_age]
print(my_list[0]) # The result gives us "Jack". If it were 1, so it will be hello, etc.

#Indexing in tuple :
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple[-2])  # The result gives us the number 8 parce que là ça commence de la fin. 

#Ranging index :
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(my_list[0:4])  # The result gives us [10, 20, 30, 40]

#string and important to note that string is a sequence of letter : 
my_name = "Rick"

print(my_name[0])
"R"

print(my_name[2])
"c"

print(my_name[-1])
"k"

print(my_name[1:3]) #"ic" de Rick

#list une liste est toujours entre []

my_hobbies = ["eat", "sleep", "code"]

my_hobbies[0]
"Eat"

my_hobbies[2]
"Code"

my_hobbies[-2]
"Sleep"

#to modify an element in the list :
print(my_hobbies)
["Eat", "Sleep", "Code"]

my_hobbies[1] = "Meditate"
print(my_hobbies)
["Eat", "Meditate", "Code"]

#to add an element in the list:
print(my_hobbies)
["Eat", "Sleep", "Code"]

my_hobbies.append = ("baseball")
print(my_hobbies)
["Eat", "Meditate", "Code"]

#to remove : 
print(my_hobbies)
["Eat", "Meditate", "Code"]

my_hobbies.remove("Meditate")

print(my_hobbies)
["Eat", "Code"]

#to with pop : 
print(my_hobbies)
["Eat", "Code"]

my_hobbies.pop(0)

print(my_hobbies)
["Code"]

#to addition list : 
my_hobbies = ["Food", "Code"]

additional_hobbies = ["Sport", "More code"]

my_hobbies + additional_hobbies 
["Food", "Code", "Sport", "More code"]

#list function : 

#lenght
fruits = ["apple","pear", "banana", "melon"]
len(fruits)
"4"

#sum
numbers = [3, 12, 1, -4]
sum(numbers)
"12"

#sorting
numbers = [3, 5, 1, 2]
sorted(numbers)
#"[1, 2, 3, 5]" ça les remet dans l'ordres

#more list methodes : 
food = ['spam', 'eggs', 'ham']
food.append('sushi')
print(food)
['spam', 'eggs', 'ham', 'sushi']

food.insert(0, 'beans')
print(food)
['beans', 'spam', 'eggs', 'ham', 'sushi']

food.extend(['bread', 'water'])
print(food)
['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']

#tuple qui utilise parenthèse
my_tuple = (5,6,7)