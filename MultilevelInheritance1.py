#here we are trying to call attributes from 1st firstly then from 2nd function and then from 3rd and then from all
class Human:
    can_breadth=True       #we can access it from every class
    def __init__(self,num_heart):
        print('calling from human class')
        self.eyes = 2
        self.heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name):
        print("Calling init from male class")
        self.name=name
    def sleep(self):
        print("I can sleep whole day")
class Boy(Male):
    #pass
    def __init__(self,can_dance):
        print("Calling init from boy class")
        self.know_dance=can_dance
    def work(self):
        super().work()     #1st method to call
        #Human.work(self)   #2nd method to call another method from another class
        print("I can code")

#boy1 = Boy(1)
#print(boy1.eyes)      #because init function is only in the humna class so it will check the sttributes there first
                        #see we are accesing attributes of humna class by calling object of boy class
#print(Boy.mro())

#boy1=Boy("Rahul")
#print(boy1.name)   #here we are calling the attributes of male class first if we don't comment above line it will give error try that also
#print(Boy.mro())

#boy1=Boy("True")
#print(boy1.can_dance)
#print(Boy.mro())

#here we can understand the mro how the sequencially the attributes or functions gets called if we want to call them all then

#here we are calling all three classes in one call
class Boy(Male):
    #pass
    def __init__(self,heart,name,can_dance):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        print("Calling init from boy class")
        self.know_dance=can_dance
    def work(self):
        super().work()     #1st method to call
        #Human.work(self)   #2nd method to call another method from another class
        print("I can code")

boy1 = Boy(1,"Rahul",True)
print(boy1.know_dance)
print(Boy.mro())
print(boy1.can_breadth)