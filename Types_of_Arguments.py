#Default

"""def Demo(name,dept='CS'):
    print(f"Hello {name}")
    print(f"Are you from {dept} department")

Demo("Mrunal")
Demo("Mrunal","IT")  #this value IT will now override the default value Cs here if we don't provide it it will take the default value



#Positional

def Demo(name,dept):
    print(f"Hello {name}")
    print(f"Are you from {dept} department")

Demo("Mrunal","IT")    #these are positional arguments at the given position it will take the value
Demo("IT","Mrunal")     #if we disturb the position it will give  messy result
"""

#KeyWord Argument

def Demo(name,dept):
    print(f"Hello {name}")
    print(f"Are you from {dept} department")

Demo(name="Mrunal",dept="IT")   #a keyword is assigned for this so it can't misunderstood
Demo(dept="CS",name="Sakshi")
