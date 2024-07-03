heights = input("Enter the heights here : ")
height_split = heights.split(",")
count = 0

for height in height_split:
    count = count +1
print(count)

for i in range(0,count):
    height_split[i]=int(height_split[i])
#print(height_split)   #successfully converted into int

total = 0
for person in height_split:
    total = total + person
print(total)

avg = total/count
print(round(avg))
