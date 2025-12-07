#Exercise 1

import math

C = 50
H = 30

input_sequence = input("Enter a sequence of comma-separated numbers: ")

numbers = input_sequence.split(",")

results = []

for number in numbers:
    D = int(number)
    Q = math.sqrt((2 * C * D) / H)
    results.append(round(Q))

print(",".join(map(str, results)))


# Exercise 2 

import random

def analyze_integers(numbers):
    """Analyzes a list of integers and prints various statistics."""

    print("a. List of numbers:", numbers)

    sorted_numbers = sorted(numbers, reverse=True)
    print("b. Sorted (descending):", sorted_numbers)

    sum_numbers = sum(numbers)
    print("c. Sum:", sum_numbers)

    first_last = [numbers[0], numbers[-1]]
    print("d. First and last:", first_last)

    greater_than_50 = [num for num in numbers if num > 50]
    print("e. Greater than 50:", greater_than_50)

    smaller_than_10 = [num for num in numbers if num < 10]
    print("f. Smaller than 10:", smaller_than_10)

    squared_numbers = [num**2 for num in numbers]
    print("g. Squared:", squared_numbers)

    unique_numbers = list(set(numbers))
    print("h. Unique:", unique_numbers, "Count:", len(unique_numbers))

    average_numbers = sum_numbers / len(numbers)
    print("i. Average:", average_numbers)

    largest_number = max(numbers)
    print("j. Largest:", largest_number)

    smallest_number = min(numbers)
    print("k. Smallest:", smallest_number)

    # Bonus: without built-in functions
    sum_bonus = 0
    largest_bonus = numbers[0]
    smallest_bonus = numbers[0]
    for num in numbers:
        sum_bonus += num
        if num > largest_bonus:
            largest_bonus = num
        if num < smallest_bonus:
            smallest_bonus = num
    average_bonus = sum_bonus / len(numbers)
    print("11. Bonus - Sum:", sum_bonus, "Average:", average_bonus, "Largest:", largest_bonus, "Smallest:", smallest_bonus)

def get_user_integers():
    numbers = []  # Correction ici: initialiser la liste numbers
    for _ in range(10):
        while True:
            try:
                num = int(input("Enter an integer between -100 and 100: "))
                if -100 <= num <= 100:
                    numbers.append(num)
                    break
                else:
                    print("Invalid input. Must be between -100 and 100.")
            except ValueError:
                print("Invalid input. Must be an integer.")
    return numbers

def generate_random_integers(count=10):
    """Generates a list of random integers between -100 and 100."""
    numbers = [random.randint(-100, 100) for _ in range(count)]
    return numbers

def generate_random_count_integers():
    """Generates a random count of integers (>=50) between -100 and 100."""
    count = random.randint(50, 100)  # Random count between 50 and 100
    return generate_random_integers(count)

# Test cases
numbers1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
analyze_integers(numbers1)

print("\n--- User Input ---")
user_numbers = get_user_integers()
analyze_integers(user_numbers)

print("\n--- Random Integers ---")
random_numbers = generate_random_integers()
analyze_integers(random_numbers)

print("\n--- Random Count Integers ---")
random_count_numbers = generate_random_count_integers()
analyze_integers(random_count_numbers)

# Exercice 3 

import re

paragraph = """
The digital age has transformed how we communicate and access information. 
Social media platforms connect people across the globe, allowing for instant 
sharing of ideas and experiences. However, this connectivity also presents 
challenges, such as the spread of misinformation and the erosion of privacy. 
Critical thinking and media literacy are essential skills for navigating 
this complex landscape. As technology continues to evolve, it is vital to 
understand its impact on our lives and to use it responsibly.
"""

# a. Number of characters
num_characters = len(paragraph)
print(f"Number of characters: {num_characters}")

# b. Number of sentences
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)
num_sentences = len(sentences)
print(f"Number of sentences: {num_sentences}")

# c. Number of words
words = re.findall(r'\b\w+\b', paragraph.lower())
num_words = len(words)
print(f"Number of words: {num_words}")

# d. Number of unique words
unique_words = set(words)
num_unique_words = len(unique_words)
print(f"Number of unique words: {num_unique_words}")

# Exerice 4

def word_frequency(input_string):
    """Calculates and prints the frequency of words in a string."""
    
    words = input_string.lower().split()
    frequency = {}

    for word in words:
        # Remove punctuation from the word
        word = ''.join(char for char in word if char.isalnum())
        if word: # Check if the word is not empty after removing the punctuation
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    # Sort the dictionary by keys (words) and print the results
    for word, count in sorted(frequency.items()):
        print(f"{word}:{count}")

# Test case
input_string = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
word_frequency(input_string)
