# check entered number is odd or even

a = int(input("Enter any number ==> "))

b = a % 2

if b:
    print("Entered " + str(a) + " is odd")
else:
    print("Entered "+str(a) + " is even")
