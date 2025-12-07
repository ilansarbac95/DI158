#exerice 1

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list1.extend(list2)
print(list1)

#exercice 2 
for number in range(1500, 2501): 
    if number % 5 == 0 and number % 7 == 0:
        print(number)

#exercice 3 
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("What is your name ? ")
    
if user_name in names: 
        index = names.index(user_name)
        print(index)
else:
    print("This name does not exist in our list")

#exercice 4 

try: 
     num1 = int(input("Enter the 1st number :"))
     num2 = int(input("Enter the 2nd number :"))
     num3 = int(input("Enter the 3rd number :"))

     greatest_number = num1

     if num2 > greatest_number:
          greatest_number = num2

    if num3 > greatest_number:
            greatest_number = num3 

    print("The greatest number is :", greatest_number)

except ValueError:
    print("Please enter a valid number")

#exerice 5 : 

alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")

# exercice 6 : 

words = []

for i in range(7):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)

letter = input("Enter a single character: ")

for word in words:
    if letter in word:
        index = word.find(letter)
        print(f"The first occurrence of '{letter}' in '{word}' is at index {index}.")
    else:
        print(f"'{letter}' does not exist in '{word}'.")

# exerice 7

numbers = list(range(1, 1000001))

print(f"Minimum value: {min(numbers)}")
print(f"Maximum value: {max(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")

# exercice 8 

input_sequence = input("Enter a sequence of comma-separated numbers: ")

number_list = input_sequence.split(",")

number_tuple = tuple(number_list)

print(number_list)
print(number_tuple)

# exercice 9 

import random

random_number = random.randint(1, 9)

try:
    user_guess = int(input("Enter a number between 1 and 9: "))

    if user_guess == random_number:
        print("Winner")
    else:
        print("Better luck next time")

except ValueError:
    print("Invalid input. Please enter a number between 1 and 9.")