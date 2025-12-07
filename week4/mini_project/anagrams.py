# anagrams.py 


from anagram_checker import AnagramChecker 


def is_valid_input(user_input): 
 """Validates the user input.""" 
 words = user_input.strip().split() 
 if len(words) != 1: 
 return False, "Only a single word is allowed." 
 if not words[0].isalpha(): 
 return False, "Only alphabetic characters are allowed." 
 return True, "" 


def main(): 
 checker = AnagramChecker() 


 while True: 
 print("\n--- Anagram Checker ---") 
 print("1. Enter a word") 
 print("2. Exit") 
 choice = input("Enter your choice: ") 


 if choice == '1': 
 user_word = input("Enter a word: ") 
 is_valid, error_message = is_valid_input(user_word) 


 if is_valid: 
 user_word = user_word.strip() 
 if checker.is_valid_word(user_word): 
 anagrams = checker.get_anagrams(user_word) 
 print(f"\nYOUR WORD :\"{user_word.upper()}\"") 
 print("This is a valid English word.") 
 if anagrams: 
 print(f"Anagrams for your word: {', '.join(anagrams)}.") 
 else: 
 print("No anagrams found for your word.") 
 else: 
 print(f"\nYOUR WORD :\"{user_word.upper()}\"") 
 print("This is NOT a valid English word.") 


 else: 
 print(error_message) 


 elif choice == '2': 
 print("Exiting program.") 
 break 
 else: 
 print("Invalid choice. Please try again.") 


if __name__ == "__main__": 
 main()