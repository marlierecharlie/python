def affiche(message):
    print(message)
    
affiche ("Hi")

# message = paramètre
# bonjour = argument

# si ne définit pas message :
# affiche() -> rien
# message d'erreur
# message est un paramètre dit obligatoir

# on peut définir des valeurs 
# par défaut pour les paramètres :

def affiche2(message="Message par défaut"):
    print(message)
    
affiche2()
    
def addition(a, b):
    return a + b

print(addition(10, 6))

# ou

print(addition(b=15, a=4))


