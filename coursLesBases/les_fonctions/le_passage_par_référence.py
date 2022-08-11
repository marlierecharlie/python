# quand on donne une valeur à une fonction,
# on passe une référence à l'objet

# def foo(param):
#     print(id(param))
    
# var = 5
# print(id(var))
# foo(param=var)
# donne 2 fois le même objet ici le nombre 5
# 2 variables différentes une dans l'espace local
# une dans l'espace global

# def foo(param):
#     param = 10
    
# var = 5
# foo(param=var)
# print(id(var))

# ici param se retrouve égal à var et
# deviennent un seul et même objet

# _____Cas des objets muables_________

from ast import fix_missing_locations


# def foo(param):
#     print(id(param))
#     param.append(1)
#     # ajoute 1 au paramètre
    
# var = []
# print(id(var))
# foo(param=var)
# print(var)
# var à été modifié, car var et param 
# pointent vers le même objet en mémoire 

# les deux variables pointent vers le même objet
# donc si on modifie cet objet dans la fonction 
# il sera aussi modifié à l'extérieur de celle-ci


def foo(param):
    test = param.copy()
    # sert à copier la référence de l'objet 
    test.append(4)
    print(test)
    print(id(test))
    
    
var = [1,2,3]
foo(param=var)
print(var)
print(id(var))
# plusieurs noms peuvent pointer vers le même
# objet

# pour revoir le chapitre : https://youtu.be/uFWYSSsJ_JE