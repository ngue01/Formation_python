import random

nombre_min=1
nombre_max=10
nombre_questions=4

def poser_question():
    a=random.randint(nombre_min,nombre_max)
    b=random.randint(nombre_min,nombre_max)
    o=random.randint(0,1)
    #0 -> +
    #1 -> *
    operateur_str="+"
    if o == 1:
        operateur_str="*"
    
    
    reponse_str=input(f"calculez: {a} {operateur_str} {b} = ")
    reponse_int=int(reponse_str)
    
    calcul=a+b
    if o == 1:
        calcul=a*b
    if reponse_int == calcul:
        
        return True
    else:
        
        return False
    
nombre_points = 0

for i in range(0, nombre_questions):
    print(f"Question n*{i+1} sur {nombre_questions}")   
    if poser_question():
        print("Reponse correcte")
        nombre_points += 1
    else:
        print("Reponse Incorrect")
    print()
print(f"votre note est de : {nombre_points} /{nombre_questions}")

moyenne = int(nombre_questions/2)
if nombre_points == nombre_questions:
    print("Excellent")
elif nombre_points == 0:
    print("Revisez vos maths")
elif nombre_points == nombre_points > moyenne:
    print("pas mal")
else:
    print(f"peut mieux faire")
    
    