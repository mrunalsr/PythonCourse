input1 = int(input("Enter the length of array : "))
list1 = []
for i in range(input1):
    input2 = int(input("Enter Elements in array : "))
    list1.append(input2)

print("The array is : ",list1)
print("The length of arraya is : ",len(list1))


if len(list1)>= 2 and list[0]+list[1] == list[-1]+list[-2]:
    middle_index = len(list1)/2;
    middle_element = list1[middle_index];
    print("Middle element",middle_element)
