#Command line arguments
#argv is not array it is list it is avialable in sys module  the arguments which are passing at the time of execution is called command line argments .
#argv[0] represents name of the program
from sys import argv
print(type(argv))
######################
from sys import argv
print("the no.of command line arguments:",len(argv))
print("the list of command line arguments:",argv)
print("command line arguments one by one:")
for x in argv:
    print(x)
