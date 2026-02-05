mylist = ["apple", "banana", "cherry"]

mylist1 = ["mango", "grape", "orange"]

#printing
print(mylist)

#append

mylist.append("kiwi")
print(mylist)

mylist.extend(mylist1)
print(mylist)

mylist.insert(3 , "pineapple")
print(mylist)

mylist.remove("apple")
print(mylist)

mylist.pop(2)
print(mylist)

mylist.clear()
print(mylist)

mylist.append("kiwi")
print(mylist.count("kiwi"))

list1 = mylist.copy()
print(mylist)
print(list1)


list1.append("strawberry")
print(mylist)
print(list1)



print(mylist.index("kiwi"))
