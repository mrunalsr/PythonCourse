#It is a hybrid inheritance problem
#It will follow the left to right than go deeper technique meaning it will check from B to C and then it will go to A for checking

class A:
    def display(self):
        print("display from A class")
class B(A):    #single
    #def display(self):
     #   print("Display from B class")
     pass
class C(A):
    def show(self):
        print("Hi from c class")
    def display(self):
        print("display from c class")
class D(B,C):    #Multiple
    pass
    #def display(self):
     #   print("display from D class")

d1 = D()
d1.display()
print(D.mro())     #this will give you idea how the class is going to check the sequence how we should check
