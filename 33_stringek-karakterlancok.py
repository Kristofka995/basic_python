#https://www.quackit.com/python/reference/python_3_string_methods.cfm

#
# szoveg='Az én barátnőm Dóra, és 15 éves.'
# print(szoveg)
#
# szoveg=szoveg.replace('15', '16').replace('Dóra','Senkimas')+" Nagyon szeretem őt."
# print(szoveg)
#
# print(szoveg.index('Senkimas'))
# print(len(szoveg))
# print(szoveg.startswith('Az'))
# print(szoveg.endswith('őt.'))
#
# print(szoveg[15:15+8])
# print(szoveg[-3:-1])
#
# szoveg2='    Ma este iszok egy hellt.  '
#
# print(szoveg2.lstrip())
# print(szoveg2.rstrip())
# print(szoveg2.strip())

adatok1='0,1,2,3,4,5,6,7,8,9'

adatok1=adatok1.split(',')
print(adatok1)

adatok2='Dóra;Betti;Erzsébet;Liza'
adatok2=adatok2.split(';')
print(adatok2)
