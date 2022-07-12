import random
# trouver un nombre aléatoire entre 0 et 100

number_to_find = random.randint(0,100)
remaining_attempts = 10
user_choice = ""

# titre 
print("*** Le jeu du nombre mystère***")

while remaining_attempts > 0 :
    #oppérateur ternaire pour ajouter s à essai si pluriel
    print(f"il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    user_choice = input("Devine le nombre")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide")
        #continue permet de revenir au début de la boucle while
        continue
    
    #permet d'écraser str user choice par un nombre entier
    user_choice = int(user_choice)
    

    if user_choice > number_to_find :
        print(f"le nombre mystere est plus petit que {user_choice}")
    elif user_choice < number_to_find :
        print(f"le nombre mystere est plus grand que {user_choice}")
    else :
        break
        
    #décrémente la variable   
    remaining_attempts -= 1
    
     
if remaining_attempts == 0 :
    print (f"""
           Dommage! Le nombre mystère était {number_to_find}
           """)
    
else :
    print(f"""Bravo! Le nombre mystère était bien {number_to_find}!
Tu as trouvé le nombre en {11-remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}
""" )

print("Fin du jeu.")
    