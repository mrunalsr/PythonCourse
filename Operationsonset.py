#Union
"""set1 = {1,2,3,4,5,5,6}
set2 = {"Ram","shyam","sita","geeta","Rupa"}
set3 = {10,11.23,34,98,45.56}

print(set1.union(set2))

print(set1 | set2 | set3)

print(set1.union(set2,set3))

print(set1.union(("Mohan","Ranga")))

print(set1.update(set2))    It will give the output as None be carefulll here
set1.update(set2)
print(set1)

set1.update(["Mohan","Ranga"])
print(set1)

set1 |= set2
print(set1)"""

#Intersection
""""set1 =  {"Ram","Shyam","Sita","geeta","Rupa"}
set2 = {"Jenny","Ram","Sita","Mrunal"}
set3 = {"Mohan","Ranga","Sita","geeta"}

print(set1.intersection(set2))

print(set1.intersection(set2,set3))  

print(set1 & set2 & set3)

set1.intersection_update(set2)
print(set1)

set2.intersection_update(set1)
print(set2)"""

#Difference
"""
set1 =  {"Ram","Shyam","Sita","geeta","Rupa"}
set2 = {"Jenny","Ram","Sita","Mrunal"}
set3 = {"Mohan","Ranga","Sita","geeta"}

print(set1.difference(set2))
print(set2.difference(set1))
print(set1.difference(set2,set3))

print(set1-set2)
print(set1 - set2 - set3)

set1.difference_update(set2)
print(set1)

set2.difference_update(set1)
print(set2)
"""

#Symmetric difference

set1 =  {"Ram","Shyam","Sita","geeta","Rupa"}
set2 = {"Jenny","Ram","Sita","Mrunal"}
set3 = {"Mohan","Ranga","Sita","geeta"}

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

print(set1 ^ set2 ^set3)

set2.symmetric_difference_update(set1)
print(set2)