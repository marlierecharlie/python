a = b = ""

while not (a.isdigit() and b.isdigit()) :
    a = (input("Entrez le premier nombres : "))
    b = (input("Entrez les deuxième nombre : "))
    if not (a.isdigit() and b.isdigit()) :
        print("Veuillez entrer deux nombres valides")
    
print(f"le résultat de l'addition {a} avec {b} est égale à {int(a) + int(b)}")

