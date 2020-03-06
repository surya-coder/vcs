#more parameaters included with in the curly braces of our syntax use the format code  syntax : {field_name: convertion} where the field_name specifies the index name and conversion refers to data type of the code
#s->string, d->decimal integers(base-10), f-floating point, c-charcter , b-binnary, o-octal, x-hexa decimal with lowecase letters after 9 , X->hexadecimal with uppercase letters after 9, e-> exponental notation
print("temprature  today {0:f} degree outside ".format(34.56))
#to limmit precession
print("my average of this {0} was {1:2f}".format("semister",78.23467))
#for no decimal places
print("my average of this {0} was {1:0f}".format("semister",78.3467))
#converts an integer to its binary
print("the {0} of 100 is {1:b}".format("birary",100))
print("the {0} of 100 is {1:o} ".format("octal",100))

print("{0:16}, is  the computer science poortal for {1:8}!".format("Geeksforgeeks","geeks"))
print(" it is {0:5} degree outside !".format(40))
print("{0:4} was founded in {1:16}!".format("OAk",2009))
print("{0:^16} was founded in {1:<4}!".format("OAK",2009))
print("{:*^20s}".format("OAK"))

def unorganiized(a,b):
    for i in range(a, b):
        print(i,i**2,i**3,i**4)
def organized(a,b):
    for i in range(a, b):
        print("{:6d} {:6d} {:6d} {:6d} ".format(i,i ** 2,i ** 3,i ** 4))

n1=int(input("Enter lower range:-\n"))
n2=int(input("Enter upper range:-\n"))
print("---------before using formaters---------")
unorganiized(n1, n2)
print()
print("---------after using formaters---------")
print()
organized(n1, n2)

