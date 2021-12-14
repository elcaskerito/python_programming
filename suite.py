#******************************************************************************#
#            UN PROGRAMME POUR AFFICHER LE NOMBRE DE VOYELLE ET CONSONE        #
#                                                                              #
#******************************************************************************#
while 1:
    
    compteurV=0

    compteurC=0
    
    text=input("\n\n ------* entrer votre text a analyser *------\n \n")
    
    voyel="aeiuoAEIUO"
    
    for txt in text:

        if txt in voyel:

            compteurV+=1

        else:

            compteurC+=1

    print("\n\n votre text comprend : ", compteurV," voyels et : ",compteurC," consones")

    sorti=input('\n\nTaper "Q" pour quitter ou Taper "Entrer" pour continuer \n')
    
    if sorti=="Q":

        print("fin de la partie")
        
        break