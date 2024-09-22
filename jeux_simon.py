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
print (sequence)

while True:
    print("rETENEZ LA SEQUENCE")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()
    