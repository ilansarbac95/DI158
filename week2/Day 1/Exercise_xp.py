# Exercice 1

def display_message():
    """Prints a sentence about what we are learning in this course."""
    print("In this course, we are learning the fundamentals of Python programming.")

# Call the function
display_message()

# Exercice 2 
def favorite_book(title):
    """Prints a message about one of my favorite books."""
    print(f"One of my favorite books is {title}")

# Call the function with a book title as an argument
favorite_book("The Adventures of Huckleberry Finn")

# Exercice 3 : 

def describe_city(city, country="Unknown"):
    """Prints a sentence describing a city and its country."""
    print(f"{city} is in {country}")

# Call the function with different arguments
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("Tokyo")  # Uses the default country value

# Exercice 4 

import random

def compare_numbers(user_number):
    """Compares a user-provided number with a random number."""

    if not 1 <= user_number <= 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        return

    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Success! You guessed the correct number.")
    else:
        print("Fail! Better luck next time.")
        print(f"Your number: {user_number}")
        print(f"Random number: {random_number}")

# Example usage
try:
    user_input = int(input("Enter a number between 1 and 100: "))
    compare_numbers(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")

# Exercice 5 

def make_shirt(size, text):
    """Prints a sentence summarizing the shirt's size and message."""
    print(f"The size of the shirt is {size} and the text is '{text}'")

# Call the function make_shirt()
make_shirt("Medium", "Python Rocks!")

# Modify the make_shirt() function with default values
def make_shirt(size="Large", text="I love Python"):
    """Prints a sentence summarizing the shirt's size and message (with defaults)."""
    print(f"The size of the shirt is {size} and the text is '{text}'")

# Call the function with default values
make_shirt()  # Large shirt with default message
make_shirt(size="Medium")  # Medium shirt with default message
make_shirt(size="Small", text="Custom message!")  # Small shirt with custom message

# Bonus: Call the function make_shirt() using keyword arguments
make_shirt(text="Keyword argument shirt!", size="Extra Large")

# Exercice 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    """Prints the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modifies the list by adding 'the Great' to each magician's name."""
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

# Call the make_great() function
make_great(magician_names)

# Call the show_magicians() function to see the modified list
show_magicians(magician_names)

# Exercice 7 : 

import random

def get_random_temp(season):
    """Generates a random temperature based on the season."""
    if season.lower() == "winter":
        lower_limit = -10
        upper_limit = 16
    elif season.lower() == "spring":
        lower_limit = 5
        upper_limit = 25
    elif season.lower() == "summer":
        lower_limit = 20
        upper_limit = 40
    elif season.lower() == "autumn" or season.lower() == "fall":
        lower_limit = 10
        upper_limit = 20
    else:
        print("Invalid season. Defaulting to -10 to 40.")
        lower_limit = -10
        upper_limit = 40

    return random.randint(lower_limit, upper_limit)

def main():
    """Gets a temperature, gives advice, and asks for a season."""
    season = input("Enter a season (summer, autumn/fall, winter, spring): ")
    temperature = get_random_temp(season)

    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 < temperature <= 23:
        print("It's a pleasant day, light jacket will do.")
    elif 23 < temperature <= 32:
        print("Warm and sunny, enjoy the day!")
    else:
        print("Hot! Drink plenty of water and seek shade.")

# Call the main function
main()

# Exercice 8 : Stars Wars <3 <3

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def run_quiz(questions):
    """Runs the Star Wars quiz and tracks correct/incorrect answers."""
    correct_count = 0
    incorrect_count = 0
    wrong_answers = []

    for question_data in questions:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_answer = input(question + " ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_count += 1
        else:
            print("Incorrect!")
            incorrect_count += 1
            wrong_answers.append({
                "question": question,
                "user_answer": user_answer,
                "correct_answer": correct_answer
            })

    return correct_count, incorrect_count, wrong_answers

def display_results(correct, incorrect, wrong_answers):
    """Displays the quiz results and wrong answers (if any)."""
    print(f"\nQuiz Results:\nCorrect answers: {correct}\nIncorrect answers: {incorrect}")

    if wrong_answers:
        print("\nWrong answers:")
        for wrong in wrong_answers:
            print(f"Question: {wrong['question']}")
            print(f"Your answer: {wrong['user_answer']}")
            print(f"Correct answer: {wrong['correct_answer']}\n")

    if incorrect > 3:
        print("You had more than 3 wrong answers. Play again to improve your Star Wars knowledge!")

# Run the quiz
correct_answers, incorrect_answers, wrong_answers_list = run_quiz(data)

# Display the results
display_results(correct_answers, incorrect_answers, wrong_answers_list)


