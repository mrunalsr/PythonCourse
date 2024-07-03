n = int(input("Enter the value of n you want : "))
for i in range(0,n):
    if i == 0:
        print("0")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
