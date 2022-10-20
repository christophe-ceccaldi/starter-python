w = input ("entrer le texte :") #variable de input
n = open("output.txt",'w') #ouvrir champ texte
n.write(w) #écrire dans fichier
n.close() #fermer édition du texte