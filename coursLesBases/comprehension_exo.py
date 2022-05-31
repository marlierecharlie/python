# exo 1 :
#liste qui réccupère que les nombres pairs (== %2)
# nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
# nombres_pairs = []
# for i in nombres :
#     if i % 2 == 0 :
#         nombres_pairs.append(i)
        
# nombres_pairs = [i for i in nombres if i % 2 == 0]
# print (nombres_pairs)

# exo2
#réccupérer uniquement les nombres positifs
# nombres = range (-10, 10)
# print (nombres)
# nombres_positifs = []
# for i in nombres : 
#     if i >= 0 : 
#         nombres_positifs.append(i)


# nombres_positifs = [i for i in nombres if i >= 0 ]
# print (nombres_positifs)

# exo3
#multiplier chaques nombres de la liste par 2
# nombres = range (5)
# nombres_doubles = []
# for i in nombres :
#     nombres_doubles.append(i*2)

# nombres_doubles = [ i*2 for i in nombres]
# print(nombres_doubles)

# exo 4
#doubler les nombres pairs, passer les impairs en négatif
nombres = range (10)
# nombres_inverses = []
# for i in nombres:
#     if i % 2 == 0:
#         nombres_inverses.append(i)
#     else : 
#         nombres_inverses.append(-i)

nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
print (nombres_inverses)