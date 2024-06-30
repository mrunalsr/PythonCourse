#Local scope
"""def display():
    a = 10
    print(a)
display()

#print(a) #it will give error because a is local variable not global

#Global Scope
a = 15
def display():
    print(a)

display()
print(a)
"""
#Both local and global scope
a = 15
def display():
    a = 10
    print(a)

display()
print(a)