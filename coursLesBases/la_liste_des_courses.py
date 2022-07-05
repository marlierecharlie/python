import sys

LISTE=[]

MENU = """choisissez parmi les 5 options suivantes : 

1: ajouter un élèment à la liste
2: retirer un élèment à la liste
3: afficher la liste 
4: vider la liste 
5: quitter
votre choix: """

Choix_du_menu = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""
    while user_choice not in Choix_du_menu:
        user_choice = input(MENU)
        if user_choice not in Choix_du_menu:
           print("Veuillez choisir une option valide: ")
             
    if user_choice == "1": 
        item = input("Entrez le nom de l'élèment à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élèment {item} a bien été ajouté à la liste.")
        
    elif user_choice == "2":
        item = input ("Entrez le nom de l'élèment à retirer de la liste : ")
        #vérifier que l'élèment est bien dans la liste
        if item in LISTE :
            LISTE.remove(item)
            print(f"L'élèment {item} a bien été retiré de la liste.")
        else : 
            print(f"L'élèment {item} n'est pas dans la liste.")
        
    elif user_choice == "3":
        #il faut faire une boucle à chaque fois pour vérifier qu'il y ait des élèments dans la liste ou non
        if LISTE :
            #ici on utilise les booléens, si Liste = true, cela signifie qu'il y a au moins un élèment dans la liste
            print("Voici le contenu de votre liste : ")
            for i, item in enumerate(LISTE, 1):
                #enumerate permet d'obtenir à la fois l'indice et l'élèments sur lequel on boucle 
                print(f"{i}. {item}")
        
        else :
            print("Votre liste est vide.")
            
        
    elif user_choice == "4":
        LISTE.clear()
        print("Le contenu de la liste a bien été effacé.")
    
    elif user_choice == "5":
        print("A bientôt!")
        sys.exit()

# sert à séparer les différentes itérations de la boucle 
    print("-" * 10)
    
    