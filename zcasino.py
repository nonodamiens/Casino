# -*-coding:utf-8 -*

# TP openclassroom Zcasino

#importation des modules nécessaires

from random import randrange
from math import ceil
from math import floor

tune=100

# On lance la boucle du programme qui se termine lorsque le joueur n'a plus de tune

while tune>0:
    print("vous avez : ",tune," $")
    mise=input("Quelle somme voulez vous parier ? : ")

# Vérification d'erreur dans la valeur indiquée pour la mise

    try:
        mise=floor(float(mise))
    except:
        print("la valeur indiquée est impossible.")
        continue

#vérification de la somme pariée

    if mise<=0 or mise>tune:
        print("La mise indiquée n'est pas valable")
    else:
        tune=tune-mise
        print("Merci pour votre mise, il vous reste : ",tune," $")

        pari=input("Choississez un nombre entre 1 et 50 :")

        try:
            pari=int(pari)
        except:
            print("la valeur indiquée n'est pas valable")
            tune=tune+mise
            continue

        if pari<=0 or pari>50:
            print("nombre impossible")
            tune=tune+mise
        else:
            
# determiner la courleur du nmbre du joueur

            if (pari/2)-floor(pari/2)!=0:
                couleurJoueur="rouge"
            else:
                couleurJoueur="noir"

            print("vous avez joué le : ",pari," ",couleurJoueur)    
            print("lancement de la roulette")
            tirage=randrange(1, 50)

# determiner si le tirage est pair ou impair

            if (tirage/2)-floor(tirage/2)!=0:
                couleur="rouge"
            else:
                couleur="noir"
          
            print("le résultat du tirage est : ",tirage," ",couleur)

# calcul des gains

            if tirage==pari:
                print("bravo vous avez gagnez : ",3*mise," $")
                tune=tune+4*mise
            elif couleur==couleurJoueur:
                print("bravo, vous avez la bonne couleur, vous gagnez :",ceil(mise/2)," $")
                tune=ceil(tune+mise+mise/2)
            else:
                print("vous avez perdu")
