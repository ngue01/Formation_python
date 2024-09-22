# Epreuve de code "Convertisseur"

"""
1 pouce = 2.54 cm
1 cm = 0.394 pouces

Exemple :
Un écran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2.54)

Voici comment votre programme doit se comporter :
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en reprécisant l'unité)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
- fin du programme.
"""

"""
effectuer_conversion : Cette fonction convertit les unités unit1 vers unit2

Return :
 True : L'utilisateur ne veut plus convertir (sortir du programme)
 False : L'utilisateur a donné une valeur à convertir
"""

def effectuer_convertion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Convertion {unit1} -> {unit2}. donnez la valeur en {unit1} (ou 'q' pour quitter) : ")
    if valeur_str == "q":
            return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR: vous devez rentrez une valeur numerique")
        print("Utilisez les point pour les nombre ")
        return effectuer_convertion (unit1, unit2, facteur)
     
    valeur_convertie =  round(valeur_float * facteur, 2)
    print(f"Resultat de la convertion: {valeur_float} {unit1} = {valeur_convertie} {unit2}")

while True:
    #menu choix de la convertion    
    print("ce programme permet des convertion d'unites")
    print("1-pouces vers centimetres")
    print("2-centimetres vers pouces")
    choice= input("Entrez votre choix (1 ou 2): ")
    if choice == "1" or choice == "2":
        break
    print("ERREUR : Vous devez choisir 1 ou 2")


while True:
    if choice == "1":
        if effectuer_convertion("pouces", "cm", 2.54):
            break
    if choice == "2":
        if effectuer_convertion("cm", "pouces", 0.394):
            break

