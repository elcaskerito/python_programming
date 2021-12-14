#******************************************************************************#
#            UN PROGRAMME POUR MONTRER L'UTILISATION DE FONCTIONS              #
#                      lambda                                                  #
#******************************************************************************#


addition = lambda x,y: x+y
# if __name__=="__main__":
a=addition(10,15)
print("res",a)

x=int(input("\n\n entrer la valeur du premier nombre \n\n"))

y=int(input("\n\n entrer la valeur du second nombre \n\n"))

print('\n\n votre resultat : ', addition(x,y))
