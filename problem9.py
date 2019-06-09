# Write a function that tests whether a string is a palindrome.

input = raw_input

a = str(input("Enter a word and check it's a palindrom or not  ==> "))

rev = ""

for x in reversed(a):
    rev += x

if a == rev:
    print "Entered word is a palindrom"
else:
    print "Entered word is not a palindrom"
