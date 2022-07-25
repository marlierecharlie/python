# déconseil fortement de l'utiliser 
# 'global'

# def get_comment(note):
#     global commentaire
#     # permet d'utiliser la variable commentaire
#     # de l'espace global
#     # a ne pas faire 
#     if note > 15:
#         commentaire = "Bravo!"
#     elif note > 10:
#         commentaire ="Peut mieux faire..."
#     elif note > 5 :
#         commentaire = "Attention!"

# commentaire = "Tu as tout faux !"

# get_comment(20)
# print(commentaire)

# ________bonne manière de faire_____

def get_comment(note):
    if note > 15:
        commentaire = "Bravo!"
    elif note > 10:
        commentaire ="Peut mieux faire..."
    elif note > 5 :
        commentaire = "Attention!"
    else :
        commentaire = "Tu as tout faux !"
    return commentaire

# ici crée une variable locale dans une 
# fonction puis retourne la valeur correspondante


commentaire = get_comment(20)
print(commentaire)

# ou meme 

# def get_comment(note):
#     if note > 15:
#         return "Bravo!"
#     elif note > 10:
#         return "Peut mieux faire..."
#     elif note > 5 :
#         return "Attention!"
#     else :
#         commentaire = "Tu as tout faux !"
#     return commentaire


# commentaire = get_comment(20)
# print(commentaire)
