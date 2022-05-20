# liste = ["1", "15", "Juliette", "22", "Pauline"]
# for element in liste :
#     if element.isdigit():
#         continue
#     print(element)
    
#continue permet de passer directement à la prochaine itération
#donc si c'est un nombre, il ne l'imprime pas 

liste = ["1", "15", "Juliette", "22", "Pauline"]
for element in liste :
    if element.isdigit():
        break
    print(element)

#break fait sortir de la boucle à l'invsere de continue qui va juste
#à l'itération sui vante 