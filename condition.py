#******************************************************************************#
#            UN PROGRAMME POUR VERIFIER SI L'ANNEE EST BISSEXTILE OU PAS       #
#                                                                              #
#******************************************************************************#
annee=int(input("entrer l'année a verifier :\n"))

bisc=False

if annee%400 ==0:
    bisc=True
elif annee%100==0:
    bisc=False
elif annee%4==0:
    bisc=True
else:
    bisc=False

# teste de bisc et affichage du resultat

if bisc:
    print("l'année est bissextile ! ")
else:
    print("l'annee saisie n'est pas bissextile")
