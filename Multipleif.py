height = int(input("Enter your height here : "))

if height>=3:
    print("Yes you are able to ride...")
    age = int(input("Enter your age here : "))
    if age < 12:
        bill = 150
        print("Please pay Rs 150")
    elif age >= 12 and age <=18 :
        bill = 250
        print("Please pay Rs 250")
    else:
        bill = 550
        print("please pay Rs 550")

    want_photo = input("Do you want to take photos inside(Y/N) ?")
    if want_photo == 'yes' or want_photo == 'Y':
        print("Please pay extra 50 Rs")
        bill = bill + 50
        print("Your total bill is Rs",bill)
    else:
        bill = bill
        print("Your total bill is : ",bill)

else:
    print("You are not able to ride...")

print("Thank you...\nVisit again")

