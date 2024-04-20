"""
Data Type - Dictionary{}
It is used to store data  in keys-values pair. 
Dict items can be any type of data, like str, int, float, bool, list, tuple, set etc.
Dict items are ordered, unindexable, changeable, and duplication is not allowed.
"""
person = {
    'name' : 'Shah',
    'age' : 27,
    'salary' : 50000,
    'status' : 'married'
}
print(person)
# gives numbers of data keys
print(len(person))
print(type(person))
# prints all the keys
print(person.keys())
# prints all the value
print(person.values())
# print the value of specified key
print(person.get('name'))
# construct dict data type
product = dict({'name':'bulb', 'price':225, 'quantity':5, 'order':'prompt'})
print(product)
print(type(product))
# x is key and y is value
for x, y in person.items():
    print(x)
    print(y)
# access the data
for x in person: print(x, "=", person[x])
if('name' in person): print(person)
# execute loop
for x in person: print(person)
# update the data
person['age'] = 30
print(person)
person.update({'age':35})
print(person)
# add new data
person['country'] = 'Pakistan'
print(person)
# remove data
person.pop('age')
print(person)