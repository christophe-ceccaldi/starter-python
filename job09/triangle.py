#créatrion de l'input
H = int (input("remplir la hauteur "))

#dessiner le triangle
a=0 #définition de la variable
for i in range (H,1,-1): #boucle def du haut du triangle jsuqu'a la base 
    print (" " * i, end="") #définir l'espace en partant de la gauche du triangle
    print ("/", end="") #coté gauche du triangle 
    print (" " * a * 2 + "\\") #espace à l'intérieur puis fermer le coté droit
    a = a+1 #redéfinition variable donc a=1 puis jusqu'a a=4


print (" /", end="")#coté gauche base du triangle 
for i in range (H-1):#boucle def du socle du triangle
    print ("__", end="")#introduction du _ pour la base
print ("\\")#coté droit de la base du triangle