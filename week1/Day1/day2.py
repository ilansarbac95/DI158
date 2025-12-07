my_name = "Jack"
my_list = [my_name, "Jack", 55, "True", "None"]
print(my_list[0])
print(my_list[-1])

location = (57.0934685737830, 44.4856740)
lat = location[0]
print(lat)

my_list = [my_name, "Frank", 55, "phone", "True", "None"]
print(my_list[0:3])

my_list = [my_name, "Frank", 55, "phone", "True", "None"]
print(my_list[1:5])

my_list = [my_name, "Frank", 55, "phone", "True", "None"]
print(my_list[1:])

my_buddy = "Ilan"
print(my_buddy[0:3])

my_buddy = "Ilan"
print(my_buddy[-1])

#2nd part
my_students = ["Ilan", "Mikhail", "Markus", "Saule"]
my_students[0] = "alex"
print(my_students)

my_students = ["Ilan", "Mikhail", "Markus", "Saule"]
my_students[0:3] = [2, 3, 5]
print(my_students)

print(dir(list))
my_students.append("markus")
my_students.append("sharon") #additional
print(my_students)

#my_students.pop[0] --> remove

data_people = ["Ilan", "Samuel", "Nathan"]
full_stack = ["Mickael", "daniel", "Gaby"]
whole_class = data_people + full_stack
print(whole_class)

#food.append
#food.insert
#food.extend

food = ['spam', 'eggs', 'ham']
food.append('sushi')
print(food)

food.insert(0, 'beans')
print(food)

food.extend(['bread', 'water'])
print(food)

#exercise
list1 = [5, 10, 15, 20, 25, 50, 20]
twenty_index = list1.index(20)
list1[twenty_index] = 200
print(list1)

#TUPLES
a_tuple = (10, 20, 30, 40)

a = a_tuple[0]
b = a_tuple[1]
c = a_tuple[2]
d = a_tuple[3]

print(a, b, c, d)

new_list = ["gabby", "markus", "sharon", "gabby"]
new_set_list = set(new_list)
print(new_set_list)

#LOOPS
#cities = ["London", "San Francisco", "Paris", "Barcelona"]

#for city in cities:
    #print("I once went to", city)

#for num in range(22):
    #print(num)

#for num in range(10,22):
    #print(num)

#for num in range(10,22, 3):
    #print(num)

sum_this_list = [1, 2, 3, 7]
print(sum(sum_this_list))

#EXERCISE LOOPS 
# Accept a number from the user and print its multiplication table
#teacher : 
user_num = int(input("Pick a number for mult table"))
for number in range(11):
    print(f"{number} x {user_num * number}")

#a_number = 1
#while a_number < 12:
    #print(a_number)
    #a_number += 1

#password = ''
#while password != 'hello-world-123':
 # password = input('What is the top secret password? ')

#print('You guessed the right password!')

#exercise while loop : 
#t = 1 
#while t <= 10:    
    #print(t)   
    #t+=1

#print("Finished")

#active = True

#while active: 
    #city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
   # if city == 'quit':
       # active = False
   # elif city == 'leave me alone':
       # active = False
   # elif city == 'stop':
       # active = False
   # else:
        #print("I'd love to go to", city)

#print("Goodbye !")

#active = True

#while True: 
   # city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
   # if city == 'quit':
       # break
   # elif city == 'leave me alone':
       # break
    #elif city == 'stop':
        #break
    #else:
       # print("I'd love to go to", city)

#print("Goodbye !")


    
