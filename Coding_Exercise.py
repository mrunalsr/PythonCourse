#Calculate BMI
height = input("Enter your height please : ")
weight = int(input("Enter your weight please : "))

BMI = weight/float(height) ** 2
round(BMI,2)
if BMI <=20:
    print("It is underweight....")
elif BMI >20 and BMI<40:
    print("It is normal...")
else:
    print("It is overweight...")
