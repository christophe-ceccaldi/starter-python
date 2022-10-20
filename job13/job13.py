w = int(input ("entré nombre entier: ")) #variable de input nb entier
fulln = open ("data.txt", "r") #variable + ouvrir le document
cmpt = fulln.read() #lire le nombres de lignes dans fichier
nb = 0 #variable comptage
list = cmpt.split() # séparer tout les mots dans une liste
for i in range (len(list)) : 
    if len(list[i]) == w :
        nb = nb+1
     
print (nb)

fulln.close

