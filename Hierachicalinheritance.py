#class Human(object):      #in python3.x it can detect the base class automaticaaly so no need to write this in bracket
#This is for function only how they work
class Human:
    def eat(self):
        print("i can eat")

class Male(Human):
    def sleep(self):
        print("I can sleep")
class female(Human):
    def work(self):
        print("I can code")

female1 = female()
female1.work()
female1.eat()
#female1.sleep()  #this will give error because there is no relation between male and female classes
male1=Male()
male1.eat()
male1.sleep()