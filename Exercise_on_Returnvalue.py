def add(a,b):
    if a ==0 and b == 0:
        return "You have enetred both values zero"
    else:
        return a+b

var1 = int(input("Enter the value of a "))
var2 = int(input("Enter the value of  b "))
addition = add(var1,var2)
print(addition)