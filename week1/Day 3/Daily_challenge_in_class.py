number = int(input("Give me a number to multiply"))
length = int(input("Give me a length to multiply"))

my_list = []
for i in range(1, length + 1):
    my_list.append(number * i)

print(my_list)
my_word = input("Give me a word" )
my_list = list(my_word)
my_set = set(my_list)
my_new_list = list(my_set)
print(''.join(my_new_list))