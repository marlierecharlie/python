from pickletools import int4
import random
# trouver un nombre aléatoire entre 0 et 100

# titre 
print("*** Le jeu du nombre mystère***")

nombre_essai = int
# il te reste 5 essais
#Il te reste {nombre_essai}.
# devine le nombre
# Veuillez entrer un nombre valide 

# le nombre mystere est plus petit que {user_choice}
# le nombre mystere est plus grand que {user_choice}
#Dommage! Le nombre mystère était {nombre_mystere}
#Fin du jeu. 

# Bravo! Le nombre mystère était bien {nombre_mystere}!
# Tu as trouvé le nombre en {nombre essai}
# Fin du jeu. 

# def variable nombre_mystere
Liste = [ _ for _ in range (1, 101)]
# print(Liste)

def selectRandom(Liste):
    return random.choice(Liste)

print(selectRandom(Liste))
while True:
    user_choice = ""
    while user_choice != selectRandom(Liste):
        user_choice = input("Veuillez entrer un nombre valide : ")
        # for i in nombre_essai :
        #     if i <= 5 :
        #         i+=1
        #     # nombre_essai(i+=1)
        #     print(f"il te reste {nombre_essai} essai")
        # if nombre_essai > 5 :
        #     break
        
    if user_choice == selectRandom(Liste) :
        print("""
          # Bravo! Le nombre mystère était bien {nombre_mystere}!
# Tu as trouvé le nombre en {nombre essai}
# Fin du jeu.""" )
    