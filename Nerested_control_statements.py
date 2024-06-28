height = int(input("Enter the height here : "))

if height>=3:
    print("You are able to ride")
    age = int(input("Enter your age please : "))
    if age >= 18:
        print("Please pay Rs.550")
    else:
        print("Please pay Rs250")
else:
    print("Sorry you are not able to ride...")

print("Thank you\nEnjoy your ride and visit again...")