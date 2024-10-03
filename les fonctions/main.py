#fonctions 

nom = "toto"
'''''
print ("Je m'appele" +  nom) #concatene la chaine
print()
print ("je m'appele ",nom ) # parametres


nom=input("Entrez notre nom :")
age= input("Entrez votre age:")
print("Mon nom est", nom, "mon age est de", age,"ans")

'''''
'''''
print("fin du programme")

#DEFINITION DE LA FONCTION
def afficher_infos_personnel():
    print("kevin")
    print("darren")

afficher_infos_personnel()
print("fin du programme")


'''''
""" nom=input("Entrez votre nom:")
age=input("Entrez votre age:") 

print("le nom de la personne est,",nom,"et son age est de",age,) """





# utilisation des parametres
""" def information_personne(nom="", age=20):
    if nom=="":
        print("vous n'avez pas donner de nom, votre age est de,",age,"ans")
    else:
        if age ==0:
            print("la personne est",nom)
        else:  
            print("la personne est",nom ,"son age est", age, "ans")
        print("Son prenom possede",len(nom),"caracteres")
    
information_personne("kevin") """

#utilisation du return 
""" def est_mageur(age):
    # Vrai ou faux
    # si l'age >= 18 =>>true sinon false
    if age >=18:
        return True
    return False



age=18
print("la personne a", age,"ans")
if est_mageur(age):
    print("la personne est Majeur")
else:
    print("la personne est Mineur")
    
    
print("Fin du programme") """

""" Recuperer_afficher_info_personne
    ->recuperer_info_personnes()
    ->afficher_infos_personne(numero_personne, nom,age)
        ->est majeur() """

def recuperer_info_personne(numero_personne):
    nom_personne=input("Nom  de la personne "+ str(numero_personne) +": ")
    age_personne=input("Age de la personne  de la personne "+ str(numero_personne) + ": ")
    return nom_personne, age_personne #retourner c'est valeur pour la fonction recuperer_et_afficher_info_personne
    
#fonction pour afficharge
def afficher_infos_personne(numero_personne, nom, age=0):
    print("la personne", numero_personne,"est",nom,"qui a pour age",age,"ans")   
    print("le nom comporte", len(nom), "caracteres")

#definir cette fonction: recuperer_et_afficher_info_personne
#Parametres: numero_personne
# rien retourner
#input et print 
#nom / age
def recuperer_et_afficher_info_personne(numero_personne):
    nom, age = recuperer_info_personne(numero_personne)
    afficher_infos_personne(numero_personne, nom, age)
    

nbr_personne=2
#input("Entrer le nombre de personne a enregistre : ")

for i in range(nbr_personne):
    recuperer_et_afficher_info_personne(i+1)
    



