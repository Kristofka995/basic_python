class person:
        #varibale fields
    name= ''
    age= ""
    gender= ""
    #methodus
    def set_age(self, value):
        self.age = value

    def set_name(self, value):
        self.name = value

    def set_gender(self, value):
        self.gender = value

#objektum peldany
Feri=person()
Feri.set_age(21)
Feri.set_name('Feri')
Feri.set_gender("Férfi")

print(Feri.age)
print(Feri.name)
print(Feri.gender)


Laci = person()
Laci.set_age(15)
Laci.set_name("Laci")
Laci.set_gender("Férfi")

print(Laci.age)
print(Laci.name)
print(Laci.gender)