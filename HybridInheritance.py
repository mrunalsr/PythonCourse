#Depth than left to right technique meaning first B than from b to a than
class A:
    def display(self):
        print("display from A class")
class B(A):    #single
    def display(self):
        print("Display from B class")
class C:
    def show(self):
        print("Hi from c class")
class D(B,C):    #Multiple
    def display(self):
        print("display from D class")

d1 = D()
d1.display()
print(D.mro())
