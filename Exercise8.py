#Check number is prime or not
def prime_or_not(number):
    if number < 0 or number == 0:
        print("invalid input")
    if number == 1:
        return "False"
    for i in range(2,number+1):
        if number%i == 0:
            return "False"
        else:
            return "True"

num = int(input("Enter the number here : "))

result = prime_or_not(num)
if result == 'True':
    print("The given number is prime")
else:
    print("The given number is not prime")