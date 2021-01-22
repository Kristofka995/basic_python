#       0       1       2           3     index
list1 = ["Betti", "Dora", "Erzsebet", "Aniko"]

print(list1[0])


print(list1[0:2])
"""
[0:2]<---contains=0(index(first)),1(index(second)), but doesn't contains the third index
if you want to get the third you can use [0:3[
"""


print(list1[-1])     #start counting from the last
#       0       1       2
#        0, 1 2   0 1 2   0 1 2
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list2[2][1])   #a 2.bol az 1est



counting = range(100)

print(counting)

print(list(counting))