"""def add(a,b):
    print("Addition : ",a+b)

add(3,4)

#now if we want 3 no addition 4 no , 5 no 6 , 7 etc all time we can't able to write function for everyone
#Arbitary Postional Argument
def add(*args):
    c = 0
    for i in args:
        c = c +i
    print("Sum of all numbers : ",c)

add(2,3)
add(5,4,8)
add(23,5,7,8,32,2,1,6)
add(-34,56,22,-78,4)


#Arbitary Keywod Argument
def info(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

info(name = "Ram",dept="IT",age=30,grades="A")

"""