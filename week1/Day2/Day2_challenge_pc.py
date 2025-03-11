#user_string = input("type a 10 char long string: ")
#if len(user_string) < 10:
    #print("string not long enough")
#elif len(user_string) > 10:
    #print("string is too long")
#else:
    #print("perfect string")

#print(user_string[0])
#print(user_string[1])

#target_string = "HelloWorld"
#constructed_string = ""

#for char in target_string:
   # constructed_string += char
   # print(constructed_string)

import random

user_string = "HelloWorld" 
user_list = list(user_string)
random.shuffle(user_list)
print(user_list)
print("".join(user_list))

import random

user_string = "HelloWorld"
user_list = list(user_string)  
random.shuffle(user_list)     
jumbled_string = "".join(user_list)  

print(jumbled_string)
