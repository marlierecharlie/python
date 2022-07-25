# retourner une valeur

def return_me_five():
    return 5

# pour réccupérer la valeur, fait une 
# assignation pour la réccupérer dabs une 
# variable :

a = return_me_five()

# return a pour effet d'arrêter la fonction
# ex : 
# def return_me_five():
#     return 5
    # print("la fonction est terminée")
# ici print est un code inateignable 

def verifier_le_fichier():
    if os.path.exists("fichier.txt"):
        return True
    return False 

# ou

def verifier_fichier():
    return os.path.exists("fichier.txt")