# Exercice 1
def inserer_element(liste, index, element):
    if 0 <= index <= len(liste):
        liste.insert(index, element)
        return liste
    else:
        print("Index hors des limites de la liste.")  # Message d'erreur amélioré
        return None

ma_liste = [1, 2, 3, 4, 5]
index_insertion = 2
element_insertion = 10

nouvelle_liste = inserer_element(ma_liste, index_insertion, element_insertion)

if nouvelle_liste:
    print(nouvelle_liste)

# exercice 2 

def compter_espaces(chaine):  
    compteur = 0
    for caractere in chaine: 
        if caractere == ' ':
            compteur += 1
    return compteur

ma_chaine = "Ceci est une chaîne de caractères avec des espaces."
nombre_espaces = compter_espaces(ma_chaine)
print(f"Le nombre d'espaces dans la chaîne est : {nombre_espaces}")

# Exercise 4
def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Exercise 5
def find_max(arr):
    if not arr:
        return None
    max_num = arr[0]
    for num in arr[1:]:
        if num > max_num:
            max_num = num
    return max_num

# Exercise 6
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Exercise 7
def list_count(arr, element):
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count

# Exercise 8
def norm(arr):
    sum_squares = 0
    for num in arr:
        sum_squares += num ** 2
    return sum_squares ** 0.5

# Exercise 9
def is_mono(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing

# Exercise 10
def longest_word(arr):
    if not arr:
        return None
    longest = ''
    for word in arr:
        if len(word) > len(longest):
            longest = word
    print(longest)

# Exercise 11
def separate_types(arr):
    integers = []
    strings = []
    for item in arr:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)
    return integers, strings

# Exercise 12
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Exercise 13
def sum_over_k(sentence, k):
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > k:
            count += 1
    return count

# Exercise 14
def dict_avg(d):
    if not d:
        return 0
    total = 0
    for value in d.values():
        total += value
    return total / len(d)

# Exercise 15
def common_div(a, b):
    divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors

# Exercise 16
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Exercise 17
def weird_print(arr):
    result = []
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            result.append(arr[i])
    return result

# Exercise 18
def type_count(**kwargs):
    types = {}
    for value in kwargs.values():
        t = type(value)
        if t in types:
            types[t] += 1
        else:
            types[t] = 1
    return ', '.join(f'{t.__name__}: {count}' for t, count in types.items())

# Exercise 19
def my_split(s, sep=' '):
    result = []
    current_word = ''
    for char in s:
        if char == sep:
            result.append(current_word)
            current_word = ''
        else:
            current_word += char
    result.append(current_word)
    return result

# Exercise 20
def password_format(s):
    return '*' * len(s)
