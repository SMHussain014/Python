"""
Data Type - Tuple()
It is used to store multiple items in a single variable. 
Tuple items can be any type of data, like str, int, float, bool, list, set etc.
Like str, tuple items can also be indexed starting from index[0].
Tuple items are ordered, but unchangeable, and allow duplication.
Items in Tuple have an unchangeable order. If we add new item, it will be added up 
at the end. One can not change, add or remove items after the creation of a tuple.
"""
week_names = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(week_names)
# indexing
print(week_names[1])
print(week_names[6])
# slicing
print(week_names[1:5])
print(len(week_names))
# construct
months_names = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print(months_names)
print(type(months_names))
months = tuple(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
print(months)
print(type(months))
# tuple can be change into list
fruits_names = ("apples", "orange", "graphes", "banana", "olive", "mango", "pear", "peach")
fruits_names = list(fruits_names)
print(fruits_names)
print(type(fruits_names))
# list can be changed into tuple
fruits_names = tuple(fruits_names)
print(fruits_names)
print(type(fruits_names))
# tuple can be changed into any type by unpacking it.
for fruit in fruits_names:
    print(fruit)
print(type(fruit))
x = (1, 2, 3, 3, 3, 4, 5, 6, 7, 7)
for n in x:
    print(n)
print(type(n))
# counts numbers of similar items
print(x.count(3))
# gives total numbers of items
print(x.index(6))