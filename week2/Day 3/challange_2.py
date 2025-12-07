#exercice 1

    #figure1
for i in range(3):
    espaces = " " * (2 - i)
    etoiles = "*" * (2 * i + 1)
    print(espaces + etoiles)

    #figure2
for i in range(5):
    espaces = " " * (4 - i) 
    etoiles = "*" * (i + 1)  
    print(espaces + etoiles)

    # figure3
for i in range(5):  
    print("*" * (i + 1)) 

for i in range(5):  
    espaces = " " * i  
    etoiles = "*" * (5 - i)  
    print(espaces + etoiles)  

# Exercice 2:

my_list = [2, 24, 12, 354, 233]  # Set a list of integers

for i in range(len(my_list) - 1):  # in the loop: iterates through the list, out of the last element
    minimum = i  # it sets the index of the minimum to the current element (i)

    for j in range(i + 1, len(my_list)):  # Inner loop: iterates through the unsorted portion of the list
        if my_list[j] < my_list[minimum]:  # If a smaller element is found
            minimum = j  # Updates the index of the minimum with the index of the smaller element

    if minimum != i:  # If a smaller element has been found and minimum updated
        my_list[i], my_list[minimum] = my_list[minimum], my_list[i]  # it changes the current element with the found minimum

print(my_list)  # it prints the sorted list


    