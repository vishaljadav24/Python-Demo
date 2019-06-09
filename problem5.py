# Multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9,

n = int(input("Enter the number and you will get multiples of three or five are considered "))
sum = 0

for x in range(1, n+1):
    if x % 3 == 0 or x % 5 == 0:
        sum += x

print "total sum is " + str(sum)
