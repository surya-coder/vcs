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