a=10
b=20


def plus1():
    print(a+b)


def plus2(a, b, c=4):
    return a+b+c


def plus3(*args):
    return sum(args) #args=arguments de akármi lehet


def greetings(*args):
    greetings = "Ennyi féle köszönés létezik:"
    for k in args:
        greetings +=k
        greetings +=","
    print(greetings[0:len(greetings)-1])
greetings("Szia","Szevassz","Csáó,""Szervusz")
#osszeadas1()

#osszeg = osszeadas2(45, 25)

#print(osszeg)

#print(osszeadas3(10,20,30,40,50,60,70,80,90,100))