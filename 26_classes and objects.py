#osztályok és objektum orientált programozás
#felhasználó által definiált tipusok/definited by user

#member variables-tag változók/mezok
class Person:
    name= ''
    kor=''
    gender= ''

p1=Person
p1.name= 'Dóra'
p1.age= '15'
p1.gender= 'Nő'

print(p1.name)
print(p1.age)
print(p1.gender)

p2= Person
p2.name= 'Laci'
p2.kora= '22'
p2.gender= 'Férfi'

print(p2.name)
print(p2.kora)
print(p2.gender)