#Arithmetic operator
"""print(5+3)
print(55-33)
print(5*3)
print(10/2)
print(10/3)
print(100%3)
print(4/2)
print(4//2)
print(2 ** 3)

print(5 +2 * 3-1 + 10/5)

#Assignment operator
a = 12
print(a)
a = a+2
print(a)
a += 2
print(a)
a,b,c = 4,5,6
print(a,b,c)

#Comparison operator
a = 5
print(a<5)
print(a==5)
print(a>3)

#Logical operator
a = 6
b = 9
print(a>4 and b<10)
print(a>7 or b<6)

c = False
print(not(c))

#Bitwise operator
a = 5
b = 4
print(a & b)   #4
print(a | b)   #5
print(a ^ b)    #1
print(~a)       #-6
print(a<<2)     #20
print(b>>2)     #1

#Identity operator
a = 5
b = 5
print(a is b)   #True      it will check the id
print(a is not b)     #False
print(a == b)       #it will check the value
print(id(a))
print(id(b))

######a = 4
print(id(a))
a = 8
print(id(a))
print(a is a)

#Membership operator
str = 'Mrunallllll'
print('l' in str)
print('al' in str)
print('L' in str)

list1 = [10,2,9,0,-1,34]
print(10 in list1)
"""
#Calculate BMI
weight = input("Enter the weight : ")
height = input("enter the height : ")

BMI = int(weight)/(int(height) ** 2)
print(BMI)

