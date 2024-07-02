#Coding EXERCISE
print("Let's calculate the love between you and your partner")
print("Please provide valid information asked below")

your_name = input("Enter your name here : ")
Partner_name = input("Enter your partner name here : ")

combine_names = your_name +" " + Partner_name
lower_case = combine_names.lower()

t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')
true = t + r + u + e

l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')
love = l + o + v + e

True_Love = int(str(true) + str(love))
#print(f"your true love score is {True_Love}% ")

if True_Love <= 10 or True_Love >= 90:
    print(f"Your love score is {True_Love} Love is very Pure. It is more than expectations")

elif True_Love >=60 and True_Love<89:
    print(f"Your love score is {True_Love}.It is pure love which will be forever")

else:
    print(f"Your love score is {True_Love}.There is just attraction. No love ")

