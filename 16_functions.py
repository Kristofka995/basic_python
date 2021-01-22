names1= "Anna", "Betti", "Dóra", "Móni", 10, True
names2= "Pista", "Álmos", "Krissz", "Ádám"


def name_printer(name_lista):
    for name in name_lista:
        if isinstance(name, str):
            print(name)
    else:
        print("Not string type, type is:" +str (type(name)))


name_printer(names1)
name_printer(names2)