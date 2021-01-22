#'is' 'is not'

number1=4
number2=5


print(number1 == number2)

number=8

if type(number) is int:                   #int-integer
    print("Int type")

if type(number) is not str:
    print("Not int type")


true = True

print(type(true) is not bool)

# class Person:
#     pass
#
# p1=Person()
# p2=Person()
#
# if type(p1) is int:
#     print("Person type")
# else:
#     print(type(p1))
#
# print(p1 is not p2)
#
#
# if isinstance(p1, Person):
#     print("Szemely tipus")