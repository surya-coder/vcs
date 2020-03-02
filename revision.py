#Ternary opearator
# if condition is true then first value should be considered else second value should be considered
a,b=10,20
x=30 if a<b else b
print(x)
#####
a=int(input("Enter the first number:"))
b=int(input("Enter second nummber:"))
min=a if a<b else b
print(min)
# nesting of ternary opearator is possibe.
a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))
c=int(input("Enter third number:"))
min=a if a<b and a<c else b if b<c else c
print(min)
#####
a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))
print("both number are equal" if a==b else "first number is less then second number "if a<b else "secod number is grater then first number ")
#####special opearators
#python defines some special opearators those are 1)identity opearator , 2) member ship opearator
#1)r1 is r2  returns true if both r1 and r2 pointing to same object , is not returns true if r1 and r2 not pointing to same object.
a=10
b=10
print(a is b)
print(a is not b)

