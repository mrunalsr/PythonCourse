#Decalring methods of dictionaries
phone_no = {
    'Ram' : 1234,
    'shyam': 3456,
    'Sita': 4567
}

print(phone_no)
print(type(phone_no))

#2nd
phone_no = dict({
    'Ram' : 1234,
    'shyam': 3456,
    'Sita': 4567
})

print(phone_no)

#3rd
phone_no= dict([('Ram',1234),('shyam',3456),('Sita',4567)])
print(phone_no)

