#exception handling (error handling)
#https://docs.python.org/3/library/exceptions.html
lista=[1, 2, 3]
#
# try:
#     #print(bla)
#     #print(lista[5])
#     #print(1 / 0)
# except NameError as e:
#     print(e, '- Nem létező változó!')
# except IndexError as e:
#     print(e, '- Tartományon kivuli index!')
# except ZeroDivisionError as e:
#     print(e, '-Nullaval osztas')
#
#
# print("Vége a programnak")
#
lista=['1', '2', '3', None, '4', '', '5', True, "Bozsi",  "12.63" ]

for i in lista:
    try:
        print(int(i) * 2)
    except:
        continue




try:
    print('bla')
except:
    print('Nem jó változónév')
# else:
#     print('Böfike koronás')
# finally:
#     print('Itt a vége ennek')