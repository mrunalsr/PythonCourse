#Break
"""count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        break
    print("Hi")
print("Out from loop")
"""
list = ['hi','hello','welcome']
names = ['krushna','ram','madhav']
for item in list:
    for name in names:
        print(item,name)
        if item == 'hello' and name == 'ram':
            break
    print("out from inner loop")
print("out from outer loop")


