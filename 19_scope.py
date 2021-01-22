#variable scope- valtozok lathatosaga, es elettartalma-lokalis es globalis valtozok

#function scope, module scope, class scope


#a=78                    #globalis
#b=47
#def test ():
#   global a,b
#    a=12                #localis
#    b=15
#    print(a, b)
#test()
#print(a)

#def test2 ():
#    for i in range (5):
#        b=54
#        pass
#    print(i)
#    print(b)
#test2()


def test():
    if True:
        c=78
    print(c)

test()