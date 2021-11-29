#******************************************************************************#
#            UN PROGRAMME POUR MONTRER L'UTILISATION DE FONCTIONS              #
#                      avec une fonction de multiplication                     #
#******************************************************************************#

# debut :  definition de la fonction avec le mot clé "def" et deux arguments (un multiplicateur et le nombre de lignes )

# nbr: represente le multiplicateur
# taill : c'est le nombre de ligne voulu

#-- debut de la fonction --#

def multi(nbr,taill):
    i=0 
    re=0
    while i<taill:
        print(i+1,'*',nbr,"=",(i + 1) * nbr)
        i+=1
        
#-- fin de la fonction --#

print("programme pour afficher les tables de multiplication\n") # message  afficher a l'utilisateur

# demander a l'utilisateur d'inserer les valeurs respectivement le multiplicateur et la taille suivi d'un separateur
nbr=int(input('entrer la table que vous vouler : \n'))
taill=int(input('la taille de votre table\n'))

print('__________________________________________\n') # afficher un séparateur
 
multi(nbr,taill) #appel de la fonction en lui passant les valeurs fournis par l'utilisateur en argument