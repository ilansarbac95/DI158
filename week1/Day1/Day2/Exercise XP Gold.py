#Exercise 1 : Hello World-I love Python
print("Hello world\nHello world\nHello world\nHello world\nI love python\nI love python\nI love python\nI love python")

#Exercise 2 
month_user = int(input("Choose a number between 1 and 12 : "))

if 3 <= month_user <= 5:
    season = "Spring"
elif 6 <= month_user <= 8:
    season = "Summer"
elif 9 <= month_user <= 11:
    season = "Autumn"
else:
    season = "Winter"

print(f"The season of the month {month_user} is : {season}")
