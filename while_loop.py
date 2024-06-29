"""count = 1
while count<=5:
    print("HIII")
    count = count+1

list1 = [1,2,4,0,5]
while list1:
    print("HIII")
    list1.pop()

count = 0
while count<=5:
    print(count)
    count += 1
else:
    print("In else block")
print("BYE")

count = 1
while count<5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    print("IN else block")       #here the control don't go in else part because we are forcing the while loop to exit


count = 1
while count < 1:
    print(count)
    count += 1

else:
    print("IN else block")"""

# cook your dish here
n = input()
count = len(n)
while count != 0:
    count += 1
print(count)