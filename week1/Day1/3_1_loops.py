name = input("Enter your mbti type ")
while name == "":
    print("You did not enter your mbti type")
    name = input("Enter your mbti type")
    print(f"Hello{name}")

age = int(input("Enter your age"))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age"))

print(f"You are {age} years old")

mbti = input("What is your favorite mbti type (q to quite): ")

while not mbti == "q":
    print(f"Your favorite mbti type is {mbti}")
    mbti = input("Enter another favorite mbti type (q to quit)")

print("bye")