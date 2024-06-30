data = {
    'Ram' : ['Dubai','Malshej','Vrindawan'],
    'sita' : ['Ayodhya','Lanka'],
    'shyam' : ['Mathura','vrindawan','Dwarika']
}
#print(data)
#print(data['Ram'])
#print(len(data))

#Dictonaries within list
data = [
    {
        'Name' : 'Ram','rollno' : 5,'age' : 25
    },
    {
        'Name' : 'sita','rollno' : 4,'age' : 22
    },
    {
        'Rank' : 2,'age' : 45,'Hobby' : 'singing'
    }
]

#print(data)
#print(data[0])
#print(data[0][1])      #Now the second time it is in dictionary so we can't access like this
print(data[0]['rollno'])

#WE can do these two types of neresting multiple time