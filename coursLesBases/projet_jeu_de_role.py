import random

points_de_degats = random.randint(5,15)
points_de_degats_enemy = random.randint(5,10)
my_lifescore = 50
ennemy_lifescore = 50
nombre_de_potions = 3
points_de_potion = random.randint(15,50)
# user_choice est une liste de caractères
user_choice = ""


while my_lifescore > 0:
    
    while ennemy_lifescore > 0 :
        
        while user_choice not in ["1","2"]:
             user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) : ")
       
        if user_choice == "1" :
            my_lifescore = my_lifescore - points_de_degats
            print(f"l'ennemi vous a infligé {points_de_degats} points de dégats.")
            print(f"Il vous reste {my_lifescore} points de vie.")
            ennemy_lifescore = ennemy_lifescore - points_de_degats_enemy
            print(f"Il reste {ennemy_lifescore} points de vie à l'ennemi.")
            
            
        elif user_choice == "2" :
            if nombre_de_potions >= 3 :
                nombre_de_potions -= 1
                my_lifescore += points_de_potion
                print(f"Vous réccupérez {my_lifescore} points de vie.")
                print(f"Il vous reste {nombre_de_potions} potions.")
                print("Vous passez votre tour!")
                my_lifescore -= points_de_degats
                print(f"l'ennemi vous a infligé {points_de_degats} points de dégats.")
                print(f"Il vous reste {my_lifescore} points de vie.")
                print(f"Il reste {ennemy_lifescore} points de vie à l'ennemi.")
            
            else :
                print("Vous n'avez plus de potions.")
                input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) : ")

    else :
        print("Tu as gagné!")

else :
    print(f"Il te reste {my_lifescore} points de vie.")
    print(f"Il reste {ennemy_lifescore} points de vie à l'ennemi.")
    print("Tu as perdu.")
    
    
    
print("Fin du jeu.")