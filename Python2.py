#String Manupulation
#capitalize() converts 1st character into uppercase
first = "hello"
second = first.capitalize()
print(second)

#casefold() = converts string into lowercase
first = "HELLO"
second = first.casefold()
print(second)

#center(width,optional fill character) = returns centered string  the fill character must be 1 char long
first = "HELLO"
second = first.center(20,'*')
second = first.center(20,'H')
print(second)

#count = number of times a specified value occurs in string
first = "HHELLO HEllo HHO"
second = first.count('H')
print(second)

#encode() = return encoded version of string
first = "HELLO"
second = first.encode('utf-8')  #ascii
print(second)

#find() = search for specific value
first = "HELLO"
second = first.find('O')
print(second)

#index() = search the string for specified value and returns the position of where it found
first = "HELLO"
second = first.index('L')
print(second)

#islower
first = "HELLO"
#second = first.islower()
second = first.lower()
second = first.isupper()
print(second)

#join() = converts the elements of an iteratble into string
words = ['Python','is','awesome']
sentence = ' '.join(words)
print(sentence)

numbers = [1,2,3]
numbers_str = ','.join(map(str,numbers))    #convert each int into str
print(numbers_str)

#partition() = returns a stringwhere the string is parted into 3 parts
#str.partition(seperator)
text = "hello world example"
result = text.partition(" ")
print(result)
#before space spcae itself and after space


#replace
str1 = "Hello world"
str2 = str1.replace("Hello","World")
print(str2)

#split()
text = "hello world example"
result = text.split()
print(result)

#map
str1 = ["1","2","3","4","5"]
str2 = map(int,str1)
print(list(str2))


