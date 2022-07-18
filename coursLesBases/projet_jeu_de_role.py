import random

points_de_degats = random.randint(5,15)
points_de_degats_enemy = random.randint(5,10)
my_lifescore = 50
ennemy_lifescore = 50
nombre_de_potions = 3
points_de_potion = random.randint(15,50)
user_choice = ""
entre = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) : ")

# chaque potion permet de réccupérer aléatoirement entre 15
# 50 pts de vie 
# mes attaquent infligent entre 5 et 10 pts de vie à l'ennemi
# l'ennemi m'inflige entre 5 et 15 pts de visiblename
# je passe le prochain tour en utilisant une potion

while my_lifescore > 0:
    
    if ennemy_lifescore > 0 :
        entre
        
        if user_choice != "1" or "2" :
            entre
        
        if user_choice == "1" :
            my_lifescore = my_lifescore - points_de_degats
            print(f"l'ennemi vous a infligé {points_de_degats} points de dégats.")
            print(f"Il vous reste {my_lifescore} points de vie.")
            ennemy_lifescore = ennemy_lifescore - points_de_degats_enemy
            print(f"Il reste {ennemy_lifescore} points de vie à l'ennemi.")
        if user_choice == "2" :
            if nombre_de_potions >= 3 :
                nombre_de_potions -= 1
                my_lifescore = my_lifescore + points_de_potion
                print(f"Vous réccupérez {my_lifescore} points de vie.")
                print(f"Il vous reste {nombre_de_potions} potions.")
                print("Vous passez votre tour!")
                my_lifescore = my_lifescore - points_de_degats
                print(f"l'ennemi vous a infligé {points_de_degats} points de dégats.")
                print(f"Il vous reste {my_lifescore} points de vie.")
                print(f"Il reste {ennemy_lifescore} points de vie à l'ennemi.")
            
            else :
                print("Vous n'avez plus de potions.")
                entre

    else :
        print("Tu as gagné!")

else :
    print(f"Il te reste {my_lifescore} points de vie.")
    print(f"Il reste {ennemy_lifescore} points de vie à l'ennemi.")
    print("Tu as perdu.")
    
    
    
print("Fin du jeu.")