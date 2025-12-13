import random
import json

# -----------------------------
#   EXERCISE 1 : RANDOM SENTENCE
# -----------------------------

WORDS_FILE = "words.txt"


def get_words_from_file(file_path):
    """Load words from a text file and return them as a list."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content.split()


def get_random_sentence(length):
    """Generate a random lowercase sentence containing `length` words."""
    words = get_words_from_file(WORDS_FILE)
    chosen_words = random.sample(words, length)
    sentence = " ".join(chosen_words).lower()
    return sentence + "." if not sentence.endswith(".") else sentence


def run_random_sentence_generator():
    print("\n=== Random Sentence Generator ===")
    user_input = input("How many words should the sentence contain (2–20)? ")

    try:
        length = int(user_input)
    except ValueError:
        print("Error: please enter a valid number.")
        return

    if length < 2 or length > 20:
        print("Error: number must be between 2 and 20.")
        return

    print("\nHere is your random sentence:")
    print(get_random_sentence(length))


# -----------------------------
#      EXERCISE 2 : JSON
# -----------------------------

sample_json = """
{
  "company": {
    "employee": {
      "name": "emma",
      "payable": {
        "salary": 7000,
        "bonus": 800
      }
    }
  }
}
"""


def run_json_exercise():
    print("\n=== JSON Exercise ===")

    # Load JSON
    data = json.loads(sample_json)

    # Access salary
    salary = data["company"]["employee"]["payable"]["salary"]
    print(f"Current salary: {salary}")

    # Add new key
    data["company"]["employee"]["birth_date"] = "1995-08-15"

    # Save to file
    output_file = "employee_data.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Modified JSON saved to {output_file}")


# -----------------------------
#         MAIN MENU
# -----------------------------

def main():
    print("\n=== Exercises XP ===")
    print("1. Random Sentence Generator")
    print("2. JSON Exercise")
    print("3. Exit")

    choice = input("Choose an option (1–3): ")

    if choice == "1":
        run_random_sentence_generator()
    elif choice == "2":
        run_json_exercise()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
