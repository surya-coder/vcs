#Iterative statements
#if we want to execute a group of statements multiple times then we should go for iterative statements
# for loop if we want to execute some action for every element in the sequence(it may be string or collection) then we should go for  iterative for loop
s="no one love solder untill enemy is at the border"
i=0
for x in s:
    print("the charcter present at",i,"index is:",x)
    i=i+1
for t in range(10):
    print("surya")
for x in range(11):
    print(x)
for x in range(21):
    if (x%2!=0):
        print(x)
for x in range(10,0,-1):
    if (x%2!=0):
        print(x)
#to print sum of numbers present inside list
d=eval(input("Enter numbers:"))
sum=0
for x in d:
    print("the sum is",sum+x)
    sum=sum+x
#while loop if we want to execute a group of statements iteratively untill some condition false then we should go for while loop
x=1
while x<=10:
    print(x)
    x=x+1

#to display sum of first n nummbers
n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("sum of",n,"numbers is:",sum)