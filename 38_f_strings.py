#String formátozas es f stringek



#old mod
text1= 'Your name is %s, and you are %d old ' % ('Andi', 37)
# print(text1)


#not too old mod
szoveg2='Your name is {}, and you are {} years old'.format("Ildi", 28)
# print(text2)


#new mod(f strings)
name= "Dóra"
age=35
text3= f"Your name is {name}, and you are {age} yo."
# print(text3)


name_dictionari={'Betti':44, 'Dóra':15, 'Andi':25, 'Jázmin':60}

for name, age in name_dictionari.items():
    print(f"Your name is {name}, and you are  {age + 5} yo.")