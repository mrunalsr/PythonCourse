import random
print("Welcome to Password Generator")
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers= ['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','$','%','&','^','*','+']
password=[]

letter_no = int(input("How many letters you want in the password : "))
numbers_no = int(input("How many numbers you want in the password : "))
symbol_no = int(input("How many symbols you want in the password : "))

#print(letter_no)
for i in range(letter_no):
    password.append(random.choice(letters))

for i in range(numbers_no):
    password.append(random.choice(numbers))

for i in range(symbol_no):
    password.append(random.choice(symbols))

#print(password)
random.shuffle(password)
password1 = "".join(password)            #The join function is used to convert the list format into string
print(f"Your password is : {password1}")
#numbers = input("Enter how many numbers you want")

