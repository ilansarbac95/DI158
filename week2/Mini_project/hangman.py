import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']

def choisir_mot():
    """Sélectionne un mot aléatoire dans la liste."""
    return random.choice(wordslist)

def masquer_mot(mot, lettres_devinees):
    """Masque le mot avec des étoiles pour les lettres non devinées."""
    mot_masque = ''
    for lettre in mot:
        if lettre in lettres_devinees:
            mot_masque += lettre
        else:
            mot_masque += '*'
    return mot_masque

def verifier_lettre(lettre, mot):
    """Vérifie si la lettre est présente dans le mot."""
    return lettre in mot

def dessiner_pendu(essais):
    """Affiche le pendu en fonction du nombre d'essais incorrects."""
    pendu = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """
    ]
    print(pendu[essais])

def obtenir_lettre_joueur():
    """Demande au joueur d'entrer une lettre."""
    while True:
        lettre = input("Devinez une lettre : ").lower()
        if len(lettre) == 1 and lettre.isalpha():
            return lettre
        else:
            print("Veuillez entrer une seule lettre.")

def verifier_victoire(mot, mot_masque):
    """Vérifie si le joueur a gagné."""
    return mot == mot_masque

# Initialisation
mot = choisir_mot()
lettres_devinees = []
essais_incorrects = 0
mot_masque = masquer_mot(mot, lettres_devinees)

# Boucle de jeu
while essais_incorrects < 6 and not verifier_victoire(mot, mot_masque):
    print(mot_masque)
    dessiner_pendu(essais_incorrects)
    lettre = obtenir_lettre_joueur()

    if lettre in lettres_devinees:
        print("Vous avez déjà deviné cette lettre.")
        continue

    lettres_devinees.append(lettre)

    if verifier_lettre(lettre, mot):
        mot_masque = masquer_mot(mot, lettres_devinees)
    else:
        essais_incorrects += 1

# Fin de partie
if verifier_victoire(mot, mot_masque):
    print("Félicitations, vous avez gagné !")
else:
    print("Vous avez perdu. Le mot était :", mot)
