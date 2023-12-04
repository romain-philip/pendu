import random

def play_hangman():
   
    words = ["python", "programmation", "ordinateur", "algorithme", "variable", "fonction", "boucle", "condition", "syntaxe", "objet", "valouzz", "flatulence", "floop", "arnaquer", "frauder", "cagoule"]

    
    word = random.choice(words)

    
    guessed_letters = []
    tries = 7

    
    while True:
       
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        
        if tries == 7:
            print("  _________     ")
            print(" |/        |    ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print("_|___            ")
        elif tries == 6:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print(" |               ")
            print("_|___            ")
        elif tries == 5:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |         |     ")
            print(" |         |     ")
            print(" |               ")
            print(" |               ")
            print("_|___            ")
        elif tries == 4:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |         |     ")
            print(" |         |     ")
            print(" |        /      ")
            print(" |               ")
            print("_|___            ")
        elif tries == 3:
            print("  _________     ")
            print(" |/        |    ")
            print(" |        (_)   ")
            print(" |         |     ")
            print(" |         |     ")
            print(" |        / \   ")
            print(" |               ")
            print("_|___            ")
        elif tries == 2:
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

        
        if "_" not in display_word:
            print("Bravo, vous avez gagné !")
            break

        
        letter = input("Entrez une lettre : ")

        
        if letter in guessed_letters:
            print("Vous avez déjà proposé cette lettre. Veuillez en choisir une autre.")
            continue

        
        guessed_letters.append(letter)

        
        if letter in word:
            print("La lettre est dans le mot !")
        else:
            print("La lettre n'est pas dans le mot.")
            tries -= 1

        
        if tries == 0:
            print("Désolé, vous avez perdu. Le mot était :", word)
            break


play_hangman()


