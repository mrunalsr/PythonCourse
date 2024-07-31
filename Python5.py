#sum of digits of a number
def sum_of_digit(number):
    number_str = str(number)
    total =0
    for digit in number_str:
        total = total + int(digit)
    return total

number  = int(input("Enter a number : "))
result = sum_of_digit(number)
print("result of sum of digits is : ",result)

print(2**3)