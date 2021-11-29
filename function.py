# une de multiplication

# debut :  definition de la fonction avec deux arguments (un multiplicateur et le nombre de lignes )

def multi(nbr,taill):
# nbr: represente le multiplicateur
# taill : c'est le nombre de ligne voulu
    i=0
    re=0
    while i<taill:
        print(i+1,'*',nbr,"=",(i + 1) * nbr)
        i+=1
# message a afficher a l'utilisateur
print("programme pour afficher les tables de multiplication\n")
# demande d'inserer les valeur respectivement le multiplicateur et la taille suivi d'un separateur
nbr=int(input('entrer la table que vous vouler : \n'))
taill=int(input('la taille de votre table\n'))
print('__________________________________________\n')
#appel de la fonction en lui passant les valeurs fournis par l'utilisateur en argument
 
multi(nbr,taill)