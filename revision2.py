#Command line arguments
#argv is not array it is list it is avialable in sys module  the arguments which are passing at the time of execution is called command line argments .
#argv[0] represents name of the program
#from sys import argv
#print(type(argv))
######################
from sys import argv
print("the no.of command line arguments:",len(argv))
print("the list of command line arguments:",argv)
print("command line arguments one by one:")
for x in argv:
    print(x)

################
#output statements
#1) print() print with out any statements print new line charcter
#2)print(strint) inside string we can use escape charcters \n ,\t, also we can use repetation opearator also if both argument are string type + opearator acts as a concatination opearator if one argument is string type and another one is int type we will get error
#3)print with varieable no.of arguments  by default output values are seperated by space if we want we can specify with sep attribute
#4)with end attribute , by default end attribute is \n if we want then we can use sep attribute
#5)print object statement we can pass any object like(list,tuple,set,etc)
#6)print(formated string)####   %i,%d,%f,%s  print("formated string:" %(varieable list))
a=10
b=20
c=30
print("a value is %i" %a)
print("b value is %d" %b)

###########
s="surya"
list=[10,20,30,40]
print("Hello %s .... The list of arguments are %s" %(s,list))
#7)print with replacement opearator
name='surya'
salary=25000
gf='no GF'
print("hello {0} Your salary is {1} and Your {2} is waiting for you ".format(name,salary,gf))



