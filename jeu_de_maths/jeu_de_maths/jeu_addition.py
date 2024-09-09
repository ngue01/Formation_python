import random

nombre_min=1
nombre_max=10

def poser_question():
    a=random.randint(nombre_min,nombre_max)
    b=random.randint(nombre_min,nombre_max)
    reponse_str=input(f"calculez: {a} + {b} =")
    reponse_int=int(reponse_str)
    if reponse_int == a+b:
        print("Reponse correcte")
    else:
        print("Reponse Incorrect")
        
poser_question()
    
    