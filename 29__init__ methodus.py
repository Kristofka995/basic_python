class Person:
    def __init__(self, name, age, gender, nationality, religion='Hindu'):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.religion = religion
        self.hello() #instead of line 18,19


    def hello(self):
        print('Hello ' + self.name)


Dora = Person('Dóra', 32, 'nő', 'Magyar', 'Keresztény')
Laci = Person('László', 47, 'Férfi', 'Roma')

# Dora.hello()
# Laci.hello()



print(type(Dora))
print(type(Laci))