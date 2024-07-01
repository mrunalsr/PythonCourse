#We can;t modify global variable inside a function so we use global keyword
"""a = 10
def display():
    global a
    a = a+1
    print(a)
display()"""

#Within function of function this global can't be used
#a = 30
def display():
    a = 20
    print("This is display method")
    print(a)
    def show():
        global a
        a = a+2
        print(a)

    #show()
    print(a)
display()


