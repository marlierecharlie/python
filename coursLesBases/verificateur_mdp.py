mdp = input ("entrez un mot de passe (min 8 caractères) : ")

mdp_trop_court = "votre mot de passe est trop court."

#si rien d'écrit
if len(mdp) == 0 :
    print (mdp_trop_court.upper()) 
    #upper pour mettre une maj début de chaîne
    
#si inf à 8 caractères
elif len(mdp) < 8 :
    print (mdp_trop_court.capitalize()) 
    #capitalize pour tt mettre en majuscules

#is digit si c'est que des nombres
elif mdp.isdigit() :
    print("Votre mot de passe ne contient que des nombres")
else:
    print ("inscription terminée")