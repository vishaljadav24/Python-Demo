# The program takes the elements of the list one by one
# Displays the average of the elements of the list.

n = int(input("Enter number of element to display ==> "))
a = []

for i in range(0, n):
    elem = int(input("Enter element "))
    a.append(elem)

avg = sum(a)/n

print("Average of elements in the list", round(avg, 2))
