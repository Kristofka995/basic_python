class Szemely:
    def __init__(self, nev, kor, neme, nemzetiség, vallás='Hindu'):
        self.nev=nev
        self.kor=kor
        self.neme=neme
        self.nemzetiség=nemzetiség
        self.vallás=vallás
        self.hello()

    def hello(self):
        print('Hello '  +self.nev)


class Alkalmazott(Szemely):

    def __init__(self, nev, kor, neme, nemzetiség, vallás, tapasztalat, megbízhatóság, végzettség):
        super().__init__(nev, kor, neme, nemzetiség, vallás)
        self.tapasztalat=tapasztalat
        self.megbízhatóság=megbízhatóság
        self.végzettség=végzettség



Eni=Alkalmazott('Enikő', 25, "Nő", "Magyar", "Ateista", 3, 8, 'Könyvelő')
Kinga=Alkalmazott('Kinga', 35, 'Nő', 'Magyar', 'Protestáns', 7, 9, 'Szakács')

print(Eni.nev)
print(Eni.végzettség)
print(Eni.vallás)


Kinga.végzettség='Autószerelő'
print(Kinga.nev)
print(Kinga.végzettség)
