#factorial of any  number
num = int(input("enter you number"))
fact = 1
if num < 0:
    print ("factorial of 0 does not exist")
if num == 0:
    print ("factorial of O is", 1)
if num > 0:
    for i in range (1, num+1):
       fact = fact * i
print ("the factorial of the given number is", fact)
