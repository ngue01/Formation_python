import time
import random
import os


def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        
print("Bienvenu dans le jeu de Simon")

# Génere de la séquence initiale
sequence=""

for i in range(4):
    chiffre = random.randint(0,9)
    sequence += str(chiffre)



clear_screen()
print("BIENVENUE DANS LE JEU DU SIMON")

score = 0
while True:
    print("RETENEZ LA SEQUENCE")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()
    
    seq_utilisateur = input("Votre reponce: ")
    if seq_utilisateur == sequence:
        score += 1
    else:
        break
    
    #input
    
    chiffre = random.randint(0,9)
    sequence += str(chiffre)
    clear_screen()
    
print("Mauvaise réponse")
print(f"la séquence était: {sequence}")
print(f"votre score final est: {score}")