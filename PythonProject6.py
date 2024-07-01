#Design a calculator using functions
print("Welcome to our scientific calculator ")
def Calculator(operation,a,b):
    if operation == 'Addition' or operation == '+':
        if a == 0 and b ==0:
            return '0'
        else:
            return a+b
    elif operation == 'Substraction' or operation == '-':
        if a == 0 and b == 0:
            return '0'
        else:
            return a - b
    elif operation == 'Multiplication' or operation == '*':
        if a == 0 or b == 0:
            return '0'
        else:
            return a * b
    elif operation == 'Division' or operation == '/':
        if a == 0 :
            return '0'
        elif b==0:
            return "Infinity"
        elif a == 0 and b ==0:
            return '0'
        else:
            return a / b
    else:
        return "Please Enter valid information"


var = input("Enter the operation you want to perform\n1)Addition(+)\n2)Substraction(-)\n3)Multiplication(*)\n4)Division(/)\nEnter here :")
var1 = int(input("Enter the 1st number here : "))
var2 = int(input("Enter the 2nd number here : "))
result =Calculator(var,var1,var2)
print(f"The {var} of these two numbers is {result} ")