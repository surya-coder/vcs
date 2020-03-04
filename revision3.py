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
