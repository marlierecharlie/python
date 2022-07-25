# les variables définies dans une fonction 
# appartiennent uniquement à cette fonction

def fonction ():
    a = 10

a = 5
fonction()
print(a)

# _____________________________________________

def foo():
    b=5
    print(locals())

a=5
foo()

# affichent à n'importe quel endroit l'espace
# global et l'espace local
# ce sont des fonctions de type dictionnaire
# d'un côté le nom de l'objet
# de l'autre, leur valeurs
globals()
locals()

# python fonctionne d'abord en local (à l'intérieur
# de la fonction) et ensuite en global