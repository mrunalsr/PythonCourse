#If we want only values from dictionaries
phone_no = {
    'Mrunal':3333,
    'Sita':5555,
    'Ram' : 8989,
    'Mohan' : 455556
}

print(phone_no.values())
print(phone_no.items())

#The data is in the form of list but the key value pairs are in the form of tuples
for i in phone_no:
    #print(i)   #This will print only key values
    print(phone_no[i])    #This will print values only

for i in phone_no.items():
    print(i)      #The items will be printed in tuples

#To copy the dictionary
phone_no2 = phone_no.copy()
print(phone_no2)

#To find length of dictionary
print(len(phone_no))