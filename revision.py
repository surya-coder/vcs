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
####
#membership operator
#returns true if the given object present in the specified collection (it may be string, list,tuple,Dict)
#in, not in
x="hello python aspirent"
print('h'in x)
print('d'not in x)
#Operator precedence
#if multiple operators present then which oparator will be evaluted first decided by opearator precedence
#->()parenenthese , ** exponential , ~- bitwise complement and unary minus opearator , *%/ // multification , modulo division floor division , + - --> addition substraction  <<, lef shift >> right shift , & bitwise and , ^ bitwise Xor  | bitwise OR  > < >= <= != == relational or comarision opearators = += -= *= Assignment opearoator is , is not -->identity opearators  in not in men=mbership opearators  not logical not  and logical and or logical or


