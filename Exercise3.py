numbers = input("Enter the numbers here : ")
numbers_list = numbers.split(" ")
print(numbers_list)

count = 0
for i in numbers_list:
    count = count+1
print(count)

for i in range(0,count):
    numbers_list[i]=int(numbers_list[i])
#print(numbers_list)

numbers_list.sort()
print("Largest no in the list is : ",numbers_list[-1])
    #a = max(numbers_list)
