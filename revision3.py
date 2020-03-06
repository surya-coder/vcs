#transfer statements
#we can use break statement inside loops to break loop execution based on some condition
#Continus useng continue statement for skip current statement and continue remining statements
n=eval(input("Enter prizes of no.of items:"))
for item in n:
    if item>20:
        print("insurence must be required ..!",item)
        break
    print(item)
cart=eval(input("Enter prizes of those items:"))
for item in cart:
    if item>25:
        print("insurence must be required",item)
        continue
    print(item)

numbers = eval(input("Enter some numbers:"))
for n in numbers:
    if n == 0:
        print("We can't do it because',it iwill raise zerodivisable error..!!", n)
        continue
    print("100/{}={}".format(n, 100 / n))

# loop with else block: if break statement not executed then with out break statement remaining statements will be executed from else block..!
cart = eval(input("Enter prizes of the items:"))
for item in cart:
    if item > 70:
        print("we cant process this item:")
        break
        print(item)
    else:
        print("Congrats item {0} processed suceusfully..!".format(item))
        print(item)

#repeat the code for every item in the sequence
##repeat the code as long as condition iis true





