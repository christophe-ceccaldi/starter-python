def crois(*args):
    # def function
    myList = []
    for i in args:
        myList.append(i)
    # ajouter le i dans my list sans écrasser
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] > myList[j]:
                myList[i], myList[j] = myList[j], myList[i]  #intervertion des éléments
    print(myList)
    # pour mettre en ordre croissant sans utiliser sort
crois(9, 24, 5, 12, 11, 8, 7, 22, 17, 27)