import sys
from tkinter import Menu
from turtle import clear

LISTE=[]

MENU = """ choisissez parmi les 5 options suivantes : 

1 : ajouter un élèment à la liste
2: retirer un élèment à la liste
3: afficher la liste 
4: vider la liste 
5:quitter
votre choix: """

Choix_du_menu = ["1", "2", "3", "4", "5"]

 while True:
     Choix_du_menu = ""
     while Choix_du_menu not in Menu:
         Choix_du_menu = input(Menu)
         if Choix_du_menu not in Menu:
             print("Veuillez choisir une option valide: ")

    if Choix_du_menu == "1": 
        item = input("Entrez le nom de l'élèment à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élèment {item} a bien été ajouté à la liste.")
        
    elif Choix_du_menu == "2":
        item = input ("Entrez le nom de l'élèment à retirer de la liste : ")
        LISTE.remove(item)
        print(f"L'élèment {item} a bien été retiré de la liste.")
        
    elif Choix_du_menu == "3":
        print(LISTE)
        
    elif Choix_du_menu == "4":
        clear(LISTE)
        print("Le contenu de la liste a bien été effacé.")
    
    else Choix_du_menu == "5":
        
    



# liste_des_courses = []

# # mettre les propositions en ligne 

# input ("choisissez parmi les 5 options suivante : 1 : ajouter un élèment à la liste")
# if i == "1":
#  print("entrez le nom d'un élèment à ajouter à la liste de courses")

# #condition 1

