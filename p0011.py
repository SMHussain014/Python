"""
Data Type - Set{}
It is used to store multiple items in a single variable. 
Set items can be any type of data, like str, int, float, bool, list, tuple etc.
Set items are unordered, unindexable, unchangeable, and duplication is not allowed.
It can be added or removed but cann't be updated.
multiplication and while loop can not run on set data type.
"""
countries_name = {"Pakistan", "India", "Sri Lanka", "Nepal", "China", "Russia", "USA", "UK", "Canada"}
print(countries_name)
print(len(countries_name))
print(type(countries_name))
for x in countries_name:
    print(countries_name)
# construct the set data type
big_countries = set({"China", "Russia", "USA", "UK", "Canada"})
print("USA" in big_countries)
print(big_countries)
print(type(big_countries))
# add/ remove (discard) and empty the data
y = big_countries.add("Japan")
print(big_countries)
z = big_countries.remove("Canada")
print(big_countries)
w = big_countries.clear()
print(big_countries)