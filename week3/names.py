# Read the file line by line
with open('names.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

# Read only the 5th line of the file
with open('names.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if len(lines) >= 5:
        print(lines[4].strip())
    else:
        print("File has less than 5 lines.")

# Read only the 5 first characters of the file
with open('names.txt', 'r', encoding='utf-8') as f:
    first_5_chars = f.read(5)
    print(first_5_chars)

# Read all the file and return it as a list of strings. Then split each word
with open('names.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    words = [word for line in content.splitlines() for word in line.split()]
    print(words)

# Find out how many occurrences of the names "Darth", "Luke" and "Lea" are in the file
with open('names.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    darth_count = content.lower().count("darth")
    luke_count = content.lower().count("luke")
    lea_count = content.lower().count("lea")
    print(f"Darth: {darth_count}, Luke: {luke_count}, Lea: {lea_count}")

# Append your first name at the end of the file
with open('names.txt', 'a', encoding='utf-8') as f:
    f.write("\nYourFirstName")  # Replace YourFirstName with your actual name

# Append "SkyWalker" next to each first name "Luke"
with open('names.txt', 'r+', encoding='utf-8') as f:
    content = f.read()
    modified_content = content.replace("Luke", "Luke SkyWalker")
    f.seek(0)
    f.write(modified_content)
    f.truncate()



newnames = []
with open ('names.txt', 'w+') as f:
    names = f.readlines()
    for names in names:
        if name = 'Luke':


import json

my_family = {
    "grandparent"