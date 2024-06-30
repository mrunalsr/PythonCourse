data = {
    'Ram' : {'rollno' : 1,'age' : 23,'course' : 'Python'},
    'shyam' : {'rollno' : 2,'age' : 22,'course' : 'C++'},
    'sita' : {'rollno' : 3,'age' : 26,'course' : 'HTML'}
}
"""print(data)
print(data['sita'])
print(data['sita']['rollno'])

#Modify the data
data['sita']['phoneno']=4567
print(data['sita'])

data['sita']['rollno'] = 6
print(data['sita'])

#Delete data from file
del data['sita']['rollno']
print(data['sita'])

#Pop method for deletion
print(data['sita'].pop('age'))
print(data['sita'])
"""
