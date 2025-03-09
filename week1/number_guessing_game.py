import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7
    for attempt in range(max_attempts):
        guess = int(input("Guess the number between 1 and 100 : "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulation! You have guessed the secret number {random_number}")
            break
    else:
        print(f"Oh pity! You have used up your 7 attempts. The secret number was {random_number}")

number_guessing_game()