# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

n = int(input("Enter the number and you will get sum of 1 to entered number "))
sum = 0

for x in range(1, n+1):
    sum += x

print  "total sum is " + str(sum)
