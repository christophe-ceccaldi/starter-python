def paranum(*args):
# definition de la fonction avec args
    mylist = []
    for i in args:
        mylist += [i]
    # += ajoute une valeur et la variable et affecte le résultat de la variable 
    for j in range(len(mylist)):
    # pour parcourir le fichier en entier len=lenght
        if (mylist[j] % 2) == 0:
        # modulo  il renvoie le restre de la division de l'opérant de gauche par l'opérant de droite
            print(mylist[j])


paranum(1,2,3,4)# afficher les nombre pairs