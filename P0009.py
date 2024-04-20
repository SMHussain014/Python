"""
There are four (04) types of built-in data used in Python to store collections of data.
The following are the data types: List [], Tuple{}, Set() and Dictionary.
Data Type - List[]
It is used to store multiple items in a single variable, i.e. dynamic length;
List items can be of any type of data, like str, int, float, bool, tuple, set etc., 
i.e. hetrogenous data types.
Like str, list items can also be indexed starting from index[0] or index[-1].
The index can be positive as well as negative.
List items are ordered, changeable, and allow duplication.
Items in List have a defined order which can not be changed. If we add new item or replace/ 
change it, it will add up at the end. If a item already exist, its duplication can be made in
List data type.
"""
fruit_items = ["apple", "orange", "mango", "mango", "grapes", "orange", "orange"]
print(fruit_items)
print(type(fruit_items))
print(len(fruit_items))
print(fruit_items[0])
print(fruit_items[2])
# slicing
print(fruit_items[1:3])
print("mango" in fruit_items)
# update/ replace list items
fruit_items[1]="banana"
print(fruit_items)
fruit_items[5]="apple"
print(fruit_items)
# add the items
fruit_items.append("waterMilen")
print(fruit_items)
fruit_items.insert(2, "pineApple")
print(fruit_items)
# remove item
fruit_items.remove("mango")
print(fruit_items)
fruit_items.pop()
print(fruit_items)
del fruit_items[6]
print(fruit_items)
# construct List
marks=list((120, 200, 150, 220, 180))
print(type(marks))
print(marks)
# reading list data type
marks=[120, 200, 150, 220, 180]
l=len(marks)
print(l)
for m in marks:
    print(m)
print("End")
i = 0
mark = [120, 200, 150, 220, 180, 250, 225, 125, 175]
while i<7:
    print(mark[i])
    i +=1
max = []
mk = [120, 110, 135, 140, 155, 105]
for m in mk:
    if m == max:
        max = m
    print(max)
even = []
numbers=[20, 50, 68, 89, 100, 119, 34, 8, 19]
for n in numbers:
    if n % 2 == 0:
# even.append()
        even = [m for m in numbers if m % 2 == 0]
    print(even)
fruits_names = ["apples", "orange", "graphes", "banana", "olive", "mango", "pear", "peach"]
# counts the similar items
print(fruits_names.count("peach"))
print(fruits_names.copy())
# empty the lists
print(fruits_names.clear())
print(fruits_names)