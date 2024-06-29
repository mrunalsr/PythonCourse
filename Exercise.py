#Pizza Ordering
print("Welcome to Pizza menia !!!")
size = str(input("Please enter size of pizza you want : "))

if size == 'large':
    bill = 300
    print("You  have to pay Rs 300 for this")
elif size == 'medium':
    bill = 200
    print("You have to pay Rs 200 for this")
else :
    bill = 100
    print("You have to pay Rs 100 for this")

quantity = int(input("Enter the quantity of pizza you want ?"))
bill = bill * quantity
print("Your bill will be : ",bill)

want_pepperoni = str(input("Do you want the pepperoni(Y/N) ?"))
if want_pepperoni == 'yes' or want_pepperoni == 'Y':
    if size == 'small':
        bill = bill + 30
        print("Your bill is : ",bill)
    else:
        bill = bill + 50
        print("your bill is : ",bill)

want_extra_cheese = str(input("Do you want extra cheese on your pizza(Y/N) ?"))
if want_extra_cheese=='yes' or want_extra_cheese== 'Y':
    bill = bill + 20
    print("Now your final bill is : ",bill)

else:
    print("Now your final bill is  : ",bill)

print("Thank you for ordering\nPlease visit again...")
