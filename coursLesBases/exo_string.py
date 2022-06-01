mot = "python"
solution = reversed (mot)
for i in solution:
    print(i)
    
# ou
# on ne peut pas directement utiliser print avec reversed, 
# il faut aussi utiliser liste c'est comme ça avec plusieurs fonctions de python 3
# print(list(reversed(mot)))
for lettre in reversed (mot):
    print (lettre)