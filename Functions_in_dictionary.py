#Let us add some data in dictionary if it is one data we can add 2 okay but 50 not easy so we use function for this
#Most important this uses append function so we need dictionary in list

data = [
            {'name' :'Ram','rollno' : 1,'age' : 23,'course' : 'Python'},
            {'name' :'Shyam','rollno' : 2,'age' : 32,'course' : 'C++'},
            {'name' :'Sita','rollno' : 3,'age' : 54,'course' : 'C'}
]

#print(data)
def add_new_data(name,rollno,age,course):
    new = {}
    new['Name'] = name
    new['rollno'] = rollno
    new['age'] = age
    new['course'] = course
    data.append(new)

add_new_data('Mohan',4,23,'Java')
print(data)