# if = Do some code only IF some condition is True
# Else do something else

age = int(input("Enter your age: "))

if age >= 120:
    print("Are you fucking kidding me!")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("Are you fucking kidding me!")
else:
    print("You must be 18+ to sign up")

response = input("Did you take the mbti test?")

if response == "Yes":
    print("Great! You will get the result soon!")
elif response == "": #elif est toujours en 2ème position
    print("Please, enter an answer")
else:
    print("Take the mbti test to see the results")

online = True
if online : 
    print("The user is online")
else:
    print("The user is offline")

mbti = input("Enter your mbti type: ")
if mbti == "":
    print("You did not enter your mbti")
else:
    print(f"Welcome to the world of MBTI, dear {mbti}")