carac = open ("data.txt", "r")
#variable + ouvrir le document(spécifier chemin si pas au mm endroit)
cnt = carac.read()
#lire le nombres de lignes dans fichier
nb = 0
#déclaration de la variable de comptage
word = cnt.split()
# séparer par tout les mots
tot=len(word)
#pour compter jusqu'au dernier mot ^pour connaitre le nombre de mots
print (tot)
#afficher le nombre de mots
carac.close
#fermer le fichier 