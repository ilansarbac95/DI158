print("strings are".upper())
print("strings are".replace("are", "is"))
print("strings")
print("strings are".replace("are", ""))

description = "Strings are..."
print(description.upper())
print(description.replace("are", "is"))
print(description.replace("are", ""))

my_age = 411
print (my_age + 123879)

bank_balance = "33000"
print(int(bank_balance))

phone_number = 532287514
print(str(phone_number))

first_name = "Ilan "
last_name = "Sarbac"

print(first_name + last_name)

print("The cow says, \"Moo\"")

x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"
print(x < y and y > 2)
print(word1 != word2)
print(bool(z), bool(word1))

#my_num = 5

#print(f"Something like {my_num + 1}")
#first_name = "ilan"
#last_name = "sarbac"
#print (f"My name is {first_name}, {last_name}")

#Name = "Alice"
#Age = 30
#City = "New York"
#print(f"Hello, {Name} You are {Age} years old and live in {City}.")

#next_week = input("What do you want to do next week? ")
#print(next_week)

#age = int(input("How old are you ? "))
#print(f"Next year I will be {age + 1} years old")

#my_height = 170

#if my_height > 200:
    #print("You are tall enough to ride!")
#elif my_height < 150:
    #print("You are too short!")
#else:
    #print("Enjoy the ride!")

#my_height = int(input("How tall are you? "))

#if my_height > 200:
    #print("You are tall enough to ride!")
#elif my_height < 150:
    #print("You are too short!")
#else:
    #print("Enjoy the ride!")

user_num = int(input("Entrez un nombre entre 1 et 100 : "))

if user_num % 15 == 0:
    print("FizzBuzz")
elif user_num % 3 == 0:
    print("Fizz")
elif user_num % 5 == 0:
    print("Buzz") 
else:
    print(user_num)
