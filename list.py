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
#with split function
l="learning python is very easy..!"
s=l.split()
print(s)
#some times we can take list inside another list those type of lists are clled nested lists.

#Accessing list of elements.
#we can access list of elements by indexing or by slicing opearator(:)
#by indexng
list=[10,20,30,"A"]
print(l[0])
#by slice opearator
#list=[startindex:endindex:stepindex]
p=[10,20,30,40,50,60,70,80,90]
print(p[3:8:2])

#list Vs mutable: once we create the list objects we can modify its content hense list objects are mutable.
n=[10,20,30,40,50]
n[1]=111
print(n)

#traversing: the sequential access of each element in the list is called traversing.

n=[10,20,30,40,50,60,70,80,90]
i=0
while i<len(n):
    print(n[i])
    i=i+1
print("by using for loop")
for i  in n:
    print(i)

print("dispying Even numbers in list:")
for i in n:
    if i%2==0:
        print(i)

#displaying elemetns in index wise:
l=["a","b","c"]
x=len(l)
for i in range(x):
    print(l[i],"at +ve index:",i,"-Ve index:",x-i)

#important functions in list:

#len() returns no of elements in the list.
#count() returns no.of occurences in the list
#index() returns index of first occurence of specified item.

#manipulating elemnets in the list
#append() to add element at the end of the list.
l=[]
l1=100
l.append(l1)
print(l)

for i in range(101):
    if i%10==0:
        print(i)
        l.append(i)
print(l)

# to insert specified item in the list with specified  index position.
p=[10,20,30,40,50]
p.insert(1,100)
print(p)
# if specified index is grater then max index the element will be inserted at last position if specified item smaller then the min index the element will be inserted at first position.
#extend() to add item one list to another list
#remove() we can use this to remove specified item from the list.if item present multiple times then only first occrence will be removed. if specified item not present in the list we get Value Error
#pop() it removes and returns last elemrnt in the list
#pop is only function which manipulates the list and returns some value
#in general we can use append and pop function to generate stack datastructure.
#pop(index)specified index we can also remove
#list objects are dynamic based on our requirement we increage or decreage the size.

#ordering elements in the list:
n=[10,20,30,40,50,60]
n.reverse()
print(n)
#sort() in list by default insertion order is preserved if we want to sort the elements of list according to default natural sorting order then we should go for sort() method.
#for numbers: default sorting order is ascending order
#for strings: default sorting order is alphabetical order
##in python2 list contain both numbers and strings then sort() function numbers followed by strings.
p=[30,40,10,24,56]
p.sort()
print(p)

#Aliasing and cloning: the process of giving another reference varieable to existing list is called aliasing.
x=[10,20,30,40,50]
y=x
print(id(x))
print(id(y))

#the problem in this approch if we want to change the content those changes will be reflected to other reference varieable.
#to overcome this problem we should go for cloning
#the process of creating exjatly duplicate indipendent objects is called cloning.
#we can impliment cloning by useing slicing or copy() function.
#slicing
x=[10,20,30,40,50]
y=x[:]
y[1]=12
print(y)
print(id(x))
print(id(y))

#by using copy() function:
x=[10,20,30,40,50,60]
u=x.copy()
u[1]=12
print(x)
print(u)
#diff b/w = and copy() :
#equal opearator is ment for aliasing
#copy() function is ment for cloning.

#using matchmatical opearators in list:
#concatination opearator
#to use + opearator both arguments should be list objects otherwise we will get error.
# we can use the repetion opearator * to repat the elements of the list specified no.of times.
x=[10,20,30]
print(x*3)
#to compare the list objects we can use the comparision opearator.
#when ever we are using relatonal opearators the first element in the list object only considered.
#membership opearator we can check the membership by using in, not in
#clear() function: to remove all elements in the list
#nested lists: some times we can take list inside another list suuch type of lists are called nested lists.
#we can access list elements using indexing just like multi dimential array elements.

#nested VS matrix:
#in python we can represent matrix by using nested lists.
n=[[30,40,60],[70,80,90],[100,120,130]]
print(n)
print("for elements in row wise:")
for r in n:
    print(r)
print("elements by matrix wise:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i],[j],end='')
print()

#list comprehension:
#it is very easy and compact way of  creating list objects from any iterable objects (like list,tuple, range, dict) based on some condition.
#list[expression item in list if condition]
s=[x*x for x in range(1,11)]
print(s)
v=[2*x for x in  range(1,6)]

word=["Balayya","Nag","chiru"]
print(word)
l=[[w.upper(),len(w)] for w in word]
print(l)









