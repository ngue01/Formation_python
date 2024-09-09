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

print("ce programme permet des convertion d'unites")
print("1-pouces vers centimetres")
print("2-centimetres vers pouces")
choice= input("Entrez votre choix (1 ou 2): ")
if choice == "1":
   valeur_str = input("Convertion pouces -> CM. donnez la valeur en pouces : ")
   valeur_float = float(valeur_str)
   valeur_convertie =  valeur_float * 2.54
   print(f"Resultat de la convertion: {valeur_float} pouces = {valeur_convertie} cm")
