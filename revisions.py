# fichier d'entraînement

# les listes 
liste = [1, 2, 3, 4]

# les dictionnaires 
# la dif entre les deux c'est aussi que l'on peut mettre plusieurs listes dans un dico : 
dict = {"école!:":"Montesquieux", "sexe":"F", "nvx":"cp"}

print(dict)

dict1 = {"élève 1":{"nom":"jean", "âge":28}, "élève2":{"nom":"juliette", "âge":23}}
print(dict1)

# _____________les opérateurs ___________
# opérations élèmentaires avec Python
1+2
1-2
1*2
# 1**2 1 à la puissance 2 
# "a"%2

# Les comparaisons : 

# "a">="b"
# "a" or "b"
# "a" and "b"

# ____________________les boucles _____________

# if, elif else 
# While, else -> attention à bien sortir de la boucle !
# for ..., if... , elif, else 

# break & continue (pour aller à l aprochaine itération)

# ___________________les compréhensions__________________________

#  je veux les longueurs des mots d'une liste de mots :
ma_liste_de_mots = [ "Cosinus", "Sinus", "Tangente", "Cotangente" ]

print([len(i) for i in ma_liste_de_mots])

#  je veux les longueurs des mots d'une liste de mots :
print([i+"hyperbolique" for i in ma_liste_de_mots])

# on peut même rajouter des conditions : Si je veux la liste des carrés
# des nombres pairs inférieurs à 15 (je rappelle qu'un nombre n est pair si et seulement si n%2==0) :

print([i**2 for i in range(16) if i%2==0])

# Si je veux récupérer la première lettre des mots d'une 
# liste commençant par une voyelle :

ma_liste_de_mots= ["maths", "info", "python", "exposant", "alpha", "fonction", "parabole", 
                   "equilateral", "orthogonal", "cercle", "isocèle" ]

print([mot[0] for mot in ma_liste_de_mots  if mot[0] in "aeiou"])