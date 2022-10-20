def paraindef (**args):
    #args permet de passer de multiples arguments et des arguments nomé à une fonction
   for i,j in args.items():
        print(i,j)
   # items() dont le rôle est de récupérer les différents paires de clefs : valeur d'un dictionnaire
paraindef(prénom = "Chris", nom = "Ceccaldi", âge = 49, ville = "Marseille")  