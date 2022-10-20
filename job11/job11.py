
nbdomains = open ("domains.xml", "r")
#variable + ouvrir le document(spécifier chemin si pas au mm endroit)
fichier = nbdomains.readlines ()
#lire le nombres de lignes dans fichier
nb = 0
#déclaration de la variable de comptage
#boucle qui parcours le fichier pour compter le nombre de fois que "domaine" apparait
for ligne in fichier :
#conditions permettant de detecter "domain"et faire en fontion que si il ne trouve pas il ne renvoi pas -1
    if ligne.find("domain") != -1 :
        nb = nb+1
#affichage du résultat
print (nb)
#fermeture du fichier
nbdomains.close()
