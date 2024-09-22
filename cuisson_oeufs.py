import time

print("Cuisson des oeufs")
print("1-Oeufs a la coque : 3 minutes")
print("2-Oeufs a la coque : 6 minutes")
print("3-Oeufs a la coque : 9 minutes")
choix = input("votre choix : ")

duree = 0
if choix == "1":
    duree = 3 * 60
if choix == "2":
    duree == 6 * 60
if choix == "3":
    duree == 9 * 60
    
while True:
    for i in range(10):
        time.sleep(1)
        duree -=1
        print(".", end="", flush=True)
    
    min = duree //60 #DIVISION ENTIERE (PAS DE VIRGULE)
    sec = duree-min*60
    print()