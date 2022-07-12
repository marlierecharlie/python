import random
# trouver un nombre aléatoire entre 0 et 100

number_to_find = random.randint(0,100)
remaining_attempts = 5
user_choice = ""

# titre 
print("*** Le jeu du nombre mystère***")

# le nombre mystere est plus petit que {user_choice}
# le nombre mystere est plus grand que {user_choice}


print(number_to_find)

while remaining_attempts > 0 :
    if user_choice != number_to_find :
        user_choice = input("""
        Devine le nombre
        """)
        print(f"il te reste {remaining_attempts} essai")
    

    if user_choice == number_to_find :
        print(f"""Bravo! Le nombre mystère était bien {number_to_find}!
Tu as trouvé le nombre en {remaining_attempts}
""" )
        
if remaining_attempts == 0 :
    print (f"""
           Dommage! Le nombre mystère était {number_to_find}
           """)
    
else :
    print("Veuillez entrer un nombre valide : ")

print("Fin du jeu.")
    