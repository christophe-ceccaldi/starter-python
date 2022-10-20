#definir les uinputs
a = int (input("remplir largeur "))
b = int (input("remplir hauteur "))
#dessiner le rezctangle
for i in range(b):
    if i ==  0 or i == b-1:
        print ("|", end="")
        for i in range(a-2):
            print ("-", end="")
        print ("|")
    else : 
        print ("|", end="")
        for i in range(a-2):
            print (" ", end="")
        print ("|") 