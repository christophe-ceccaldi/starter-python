#####valeurs input
a = int(input ("entrée une première valeur "))
b = int(input ("entrée une seconde valeur "))
if a > b :
    for i in range (a , b, -1) :
        print (i)
elif a < b :
    for i in range (a , b ) :
        print (i)
else:
    print ("Valeurs égales")
