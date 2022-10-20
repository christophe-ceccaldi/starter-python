from logging import shutdown


a = input ("> ")
while a != "Au revoir" :
    if a == "Bonjour" :
        print ("Bonjour à toi")
        a = input ("> ")
    else : 
        a = input ("> ")
exit()
