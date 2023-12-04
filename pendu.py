import random

def play_hangman():
    # Liste de mots à deviner
    words = ["python", "programmation", "ordinateur", "algorithme", "variable", "fonction", "boucle", "condition", "syntaxe", "objet", "valouzz", "flatulence", "floop", "arnaquer", "frauder", "cagoule"]

    # Choisir un mot aléatoire
    word = random.choice(words)

    # Initialiser les variables
    guessed_letters = []
    tries = 6

    # Boucle principale
    while True:
        # Afficher le mot à deviner
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        # Dessiner le pendu
        if tries == 6:
            print("  _________     ")
            print(" |/        |    ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print("_|___            ")
        elif tries == 5:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print("_|___            ")
        elif tries == 4:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |         |     ")
            print(" |         |     ")
            print(" |               ")
            print(" |               ")
            print("_|___            ")
        elif tries == 3:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |         |     ")
            print(" |         |     ")
            print(" |        /      ")
            print(" |               ")
            print("_|___            ")
        elif tries == 2:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |         |     ")
            print(" |         |     ")
            print(" |        / \   ")
            print(" |               ")
            print("_|___            ")
        elif tries == 1:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |        /|     ")
            print(" |         |     ")
            print(" |        / \   ")
            print(" |               ")
            print("_|___            ")
        elif tries == 1:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |        /|\    ")
            print(" |         |     ")
            print(" |        / \   ")
            print(" |               ")
            print("_|___            ")
        else:
            print("Désolé, vous avez perdu. Le mot était :", word)
            break

        # Vérifier si le joueur a gagné
        if "_" not in display_word:
            print("Bravo, vous avez gagné !")
            break

        # Demander une lettre
        letter = input("Entrez une lettre : ")

        # Vérifier si la lettre a déjà été proposée
        if letter in guessed_letters:
            print("Vous avez déjà proposé cette lettre. Veuillez en choisir une autre.")
            continue

        # Ajouter la lettre à la liste des lettres proposées
        guessed_letters.append(letter)

        # Vérifier si la lettre est dans le mot
        if letter in word:
            print("La lettre est dans le mot !")
        else:
            print("La lettre n'est pas dans le mot.")
            tries -= 1

        # Vérifier si le joueur a perdu
        if tries == 0:
            print("Désolé, vous avez perdu. Le mot était :", word)
            break

# Lancer le jeu
play_hangman()