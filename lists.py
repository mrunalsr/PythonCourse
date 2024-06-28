roll_no = [10,4,-3,98,34,0,10,2,5,2,89]
"""print(roll_no)
#names = ["Mrunal","Mansi","Jyoti","Satish"]
#print(names)
#mix_list = [1,10,-3,"Mrunal",10.39,True,0]
#print(mix_list)
print(roll_no[3])
print(roll_no[-2])
print(len(roll_no))

#Slicing of list
print(roll_no[0:4])
print(roll_no[0:])
print(roll_no[2:7])
print(roll_no[:5])
print(roll_no[1:])
print(roll_no[2:7:2])

#Sort list
#print(roll_no.sort())  the o/p will be NOne
roll_no.sort()
print(roll_no)

#Reverse List
roll_no.reverse()
print(roll_no)

#MinMax in list
print(max(roll_no))
print(min(roll_no))
print(sum(roll_no))
print(len(roll_no))

#TO add some items in list there are 3 methods
#append
roll_no.append(45)
print(roll_no)

#Insert
roll_no.insert(3,96)
print(roll_no)

#extend
roll_no.extend([11,22,33,44,55])
print(roll_no)

#Change the data in the list
print(roll_no)
print(roll_no[3]=97) # it will give error!!!!!!!!!!!!!!
roll_no[3]=97
print(roll_no)

roll_no[2:4]=[38,37]
print(roll_no)

#Remove Method
print(roll_no)
roll_no.remove(10)
print(roll_no)
roll_no.pop()
print(roll_no.pop())
print(roll_no)
print(roll_no.pop(3))
print(roll_no)"""
