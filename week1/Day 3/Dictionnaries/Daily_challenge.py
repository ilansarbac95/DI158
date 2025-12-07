def create_letter_index_dict(word):
    """
    Crée un dictionnaire qui stocke les indices de chaque lettre dans une liste.

    Args:
        word (str): Le mot à partir duquel créer le dictionnaire.

    Returns:
        dict: Un dictionnaire où les clés sont les lettres et les valeurs sont les listes d'indices.
    """
    letter_indices = {}
    for index, letter in enumerate(word):
        if letter not in letter_indices:
            letter_indices[letter] = [index]
        else:
            letter_indices[letter].append(index)
    return letter_indices

# Demande à l'utilisateur un mot
word = input("Entrez un mot : ")

# Crée et affiche le dictionnaire
result_dict = create_letter_index_dict(word)
print(result_dict)

#class

word = input("Enter a word: ")
word_dict = {}

for i in range(len(word)):  # Correction : Utiliser len() au lieu de lien()
    if word[i] in word_dict:  # Correction : Utiliser word[i] au lieu de i word[i]
        word_dict[word[i]].append(i)
    else:
        word_dict[word[i]] = [i]

print(word_dict)