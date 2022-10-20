def order(*args):
# definition de la fonction avec args
    mylist = []
    for i in args:
        mylist += [i]
    mylist.sort()
    print (mylist)

order(5,1,2,3,4)