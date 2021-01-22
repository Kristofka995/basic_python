# 'in' membership operator-tagsagi operator

phrase= 'Bagoly mondja verébnek nagyfejű'

if 'Veréb' in phrase:
    print('Találat')

name_list=['Betti', 'Dóra', 'Anna', 'Ildi']
if 'Dóra' in name_list:
    print('Találat')

if 'Dóra' not in name_list:
    print('Nincs Találat')


name_dictionary={'Betti':44, 'Dóra':15, 'Andi':25, 'Jázmin':60}

if 'Dávid' not in name_dictionary:
    print('Nincs Találat')



szamok1=[1,2,3,4,5,6,7]
szamok2=[0,2,4,6,8,7]


azonos_szamok=[]
egyedi_szamok=[]
for szam in szamok1:
    if szam not in szamok2:
        egyedi_szamok.append(szam)

print(egyedi_szamok)