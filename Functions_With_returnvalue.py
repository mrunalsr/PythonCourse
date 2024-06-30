#Return one value
"""def add(a,b):
    c = a+b
    return c

output = add(3,4)
print(output)
"""

#Return multiple values

import statistics
def calculate(list1):
    return statistics.mean(list1),statistics.median(list1), statistics.mode(list1)

#print(calculate([23,55,44,77,66,66,66]))
#OR

a,b,c = calculate([23,55,44,77,66,66,66])
print(f"Mean of the list is : {a},Median of list is : {b},Mode of list is : {c}")