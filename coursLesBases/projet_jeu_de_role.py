import random

my_lifescore = 50
ennemy_lifescore = 50
nombre_de_potions = 3
SKIP_TURN = False


while my_lifescore > 0:
    
    if SKIP_TURN:
        print("Vous passez votre tour")
        SKIP_TURN = False
        
    else :
        user_choice = ""
        while user_choice not in ["1","2"]:
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) : ")
            potion_health = random.randint(15, 50)
       
        if user_choice == "1" :
            your_attack = random.randint(5, 10)
            ennemy_lifescore -= your_attack
            print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi.")   
            
        elif user_choice == "2" :
            if nombre_de_potions > 0 :
                my_lifescore += potion_health
                nombre_de_potions -= 1
                print(f"La potions t'as fait gagner {potion_health} points de vie")
                print(f"Il te reste maintenant {nombre_de_potions} potions.")
                SKIP_TURN = True
            else :
                print("Vous n'avez plus de potions.")
                continue

    if ennemy_lifescore <= 0 :
        print(f"Il vous reste {my_lifescore} points de vie.")
        print("Il reste 0 points de vie à l'ennemi.")
        print("Tu as gagné!")
        break
    
    enemy_attack = random.randint(5, 15)
    my_lifescore -= enemy_attack
    print(f"L'ennemi vous a infligé {enemy_attack} points de dégats.")
    
    if my_lifescore <= 0 :
        print("Il vous reste 0 points de vie.")
        print(f"Il reste {ennemy_lifescore} points de vie à l'ennemi.")
        print("tu as perdu")
        break 
    
    print(f"Il vous reste {my_lifescore} points de vie.")
    print(f"Il reste {ennemy_lifescore} points de vie à l'ennemi.")
    print("-" * 50)
    
print("Fin du jeu.")