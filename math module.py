# math module
#a module is a collection of functions , varieables , classes etc
#math module that contain several matchmatical functions to perform on it
import math
print(math.sqrt(12))
# we can aliasing using as keyword.
import math as m
print(m.sqrt(12))
#we can import particuler member as below follows
from math import sqrt
#if importing specific meber no need to write math.pi like that  if we are dooing like that we get name error
#enter the employee details as a dynamic data from the keyboard
eno=int(input("enter employee number:"))
ename=input("enter employee name:")
esal=int(input("Enter the employee salary:"))
eadder=input("Enter the employee address:")
married=input("Employee married?[True | False]")
print("please conform the details:")
print("Employee Number:",eno)
print("Employee Name:",ename)
print("Employee salary:",esal)
print("Employee address:",eadder)
print("Employee married:",married)
##
a,b=[int(x) for x  in input("Enter two stings :").split()]
print("the product is :",a*b)
#split can take space as seperator but we have to provide some thing to it
#float
a,b=[float(x) for x in input("enter two numbers:").split(',')]
print("the product is:",a*b)
#eval() eval function take values as string and evaluates the result
e=eval(input("Enter any expression"))
print(e)
#eval() can evalutes the input to a list tuple set etc based on provided  input
