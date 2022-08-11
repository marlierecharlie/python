# liste : on ne peut accéder à leur contenu que avec les indices 

from logging.config import dictConfig


dictionnaire = {
                0:{"prenom":"Paul",
                "profession":"Ingénieur",
                "ville":"Paris"},
                1:{"prenom":"Julie",
                   "profession":"architecte",
                   "ville":"Marseille"},
                2:{"prenom":"Pierre",
                   "profession":"Plombier",
                   "ville":"Nantes"}
}

# les dictionnaires peuvent être imbriqués les uns dans les autres
# ici il conteint trois clés (0,1 et 2), les trois clés ont elles même 
# trois autres clés (prennom, nom et ville).

# chaque clé d'un dictionnaire doit être unique
# on ne peut donc pas avoir : 
#  d={"prenom":"Paul","prenom":"Julie"}

# ________________________RECUPERER UNE VALEUR__________________________

d = {"clé":"valeur"}
d["clé"]

# dans le premier exemple :
print(dictionnaire[0]["ville"])

# cette méthode retourne une erreur si la clé utilisée n'est pas dans
# notre dictionnaire, pour éviter ça, utiliser la méthode "get":

print(dictionnaire.get("arbre"))
# cela retourne none. 

# on peut en profiter pour lui donner une valeur par défaut à nous
# retourner si la clé n'existe pas :
print(dictionnaire.get("vautour", "cette clé n'est pas dans le dictionnaire"))

# _________________MODIFIER UNE VALEUR DANS LE DICTIONNAIRE_______________

dictionnaire [0]["prenom"] = "Sabine"
# la réccupérer avec les crochets et lui réassigner une valeur
print(dictionnaire [0]["prenom"])

# un dictionnaire est un objest muable, en le réaffichant on verra
# qu'il a été modifié :
print(dictionnaire)

# ______________________AJOUTER ET SUPPRIMER DES CLES_______________________

# ajouter une clé:
dictionnaire[0]["age"]=30
print(dictionnaire)

# supprimer une clé :
del dictionnaire [0]["age"]
print(dictionnaire)

# si on supprime une clé qui n'existe pas dans notre dico, on aura une 
# erreur, voici comment s'en prémunir :
if "clé" in d:
    del d["clé"]

print(d)

# ___________________PARCOURIR/BOUCLER SUR UN DICTIONNAIRE__________________

# mm méthode pour réccupérer toutes les clés ou toutes les valeurs
print(dictionnaire.keys())
print(dictionnaire.values())

# réccupérer les clés et les valeurs
print(dictionnaire.items())


