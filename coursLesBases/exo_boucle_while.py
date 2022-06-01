# continuer = "o"
# while continuer == "o":
#    print("on continue !")
#    continuer = input("voulez-vous continuer? o/n")

# ou

continuer = "o"
while continuer == "o":
    print("on continue !")
    resultat = input("voulez-vous continuer? o/n")
    if resultat != "o":
        print("on arrête")
        break 