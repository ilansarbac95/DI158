#Exercice 1 : 

input_string = input(" Entrez une série de séquences de mots : ")
words = input_string.split(",")  
sorted_words = sorted(words)  
output_string = ",".join(sorted_words)  
print(output_string)

#Exercice 2 : 

def longest_word(sentence):
    words = sentence.split()  
    longest = ""  

    for word in words:  
        if len(word) > len(longest): 
            longest = word  

    return longest 

# Some Exemples
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
