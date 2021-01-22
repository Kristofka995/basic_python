class Person:
    def __init__(self, name, age, gender, nationality, religion='Hindu'):
        self.name=name
        self.age=age
        self.gender=gender
        self.nationality=nationality
        self.religion=religion
        self.hello()  #24,25.sor helyett

    def hello(self):
        print('Hello ' + self.name)


class Employee(Person):
    experience=4
    trustable=8
    education='Könyvelő'

Eni = Employee('Enikő', 25, "Nő", "Magyar", "Hindu")
Kinga = Employee('Kinga', 35, 'Nő', 'Magyar', 'Protestáns')

print(Eni.name)
print(Eni.education)


Kinga.education='Autószerelő'
print(Kinga.name)
print(Kinga.education)
