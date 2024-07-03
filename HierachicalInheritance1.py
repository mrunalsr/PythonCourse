#here we are learning attributes how they work
"""class Human:
    def __init__(self,name,age):
        print("Calling from humna class")
        self.name=name
        self.age=age
    def showdetails(self):
        print(f"name: {self.name},age : {self.age}")
    def eat(self):
        print("i can eat")

class Male(Human):
    def sleep(self):
        print("I can sleep")
class female(Human):
    def work(self):
        print("I can code")

#female1 = female()    #if we write like this it will give error because in above code we pass 2 arguments in human init function so we have to pass them in female also
female1=female("Mrunal",21)   #now okay
female1.eat()
print(female1.age)
female1.showdetails()










#here we are learning attributes how they work in male class now step by step
class Human:
    def __init__(self,name,age):
        print("Calling from humna class")
        self.name=name
        self.age=age
    def showdetails(self):
        print(f"name: {self.name},age : {self.age}")
    def eat(self):
        print("i can eat")

class Male(Human):
    def __init__(self,m_name,age,location):  #we can access this name and age from human
        print("Calling from male class")
        Human.__init__(self,m_name,age)  #we are trying to access the name and age from human in init function we can give any name here but same as init function int male clas
        self.location=location
    def sleep(self):
        print("I can sleep")
class female(Human):
    def work(self):
        print("I can code")

#the female part will work fine here also because no connection with male
#female1 = female()    #if we write like this it will give error because in above code we pass 2 arguments in human init function so we have to pass them in female also
#female1=female("Mrunal",21)   #now okay
#female1.eat()
#print(female1.age)
#female1.showdetails()
male1 =Male("Mrunal",21,"delhi")
print(Male.mro())

"""




class Human:
    def __init__(self,name,age):
        print("Calling from humna class")
        self.name=name
        self.age=age
    def showdetails(self):
        print(f"name: {self.name},age : {self.age}")
    def eat(self):
        print("i can eat")

class Male(Human):
    def __init__(self,m_name,age,location):  #we can access this name and age from human
        print("Calling from male class")
        Human.__init__(self,m_name,age)  #we are trying to access the name and age from human in init function we can give any name here but same as init function int male clas
        self.location=location
    def sleep(self):
        print("I can sleep")
class female(Human):
    def __init__(self,name,age,can_dance):
        print("Calling from female class")
        super().__init__(name,age)
        self.know_dancing=can_dance

    def showdetails(self):
        Human.showdetails(self)
        print(f"Know dancing:{self.know_dancing}")
    def work(self):
        print("I can code")

#the female part will work fine here also because no connection with male
#female1 = female()    #if we write like this it will give error because in above code we pass 2 arguments in human init function so we have to pass them in female also
female1=female("Mrunal",21,True)   #now okay
female1.eat()
female1.showdetails()
print(female1.age)
#print(female1.age)
#female1.showdetails()
#male1 =Male("Mrunal",21,"delhi")
#print(Male.mro())

