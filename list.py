#if we want to represent a group of individual objects as a single entity where incercion order is preserved and duplicates are allowed , then we should go or list data structure.
#incertion order is preserved, duplicates are allowed, hetro genious objects are allowed , list is dynamic because based on our requirement we can increage the order or decreage the order hence index will play very important role.

#creation of list objects
# we can create the empty list objects.
list=[]
print(list)
#if we know the elements already.
list=[10,20,30,40]
print(list)

#dynamic input
list=eval(input("Enter list of objects:"))
print(list)
#with list function
l=list(range(0,10,2))
print(l)
#with split function
l="learning python is very easy..!"
s=l.split()
print(s)
#some times we can take list inside another list those type of lists are clled nested lists.
