#class Human(object):
#for functions here
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def sleep(self):
        print("I can sleep whole day")
class Boy(Male):
    #pass
    def work(self):
        super().work()     #1st method to call
        #Human.work(self)   #2nd method to call another method from another class
        print("I can code")

class Programmer(Boy):
    def work(self):
        print("I can write a program")
boy1 = Boy()
#boy1.eat()
boy1.work()
prog1 = Programmer()
prog1.work()