# Write three functions that compute the sum of the numbers in a list:
# using a for-loop, a while-loop and recursion

a = [424, 5, 24, 45, 32, 42, 65, 35, 75, 231]


def sumUsingForLoop():
    sum = 0
    for x in a:
        sum += x
    print str(sum)


def sumUsingWhileLoop():
    i = 0
    sum = 0
    while i < len(a):
        sum += a[i]
        i += 1
    print str(sum)


index = 0
def sumUsingRecursion(sum = 0):
    global index
    sum += a[index]
    index += 1
    if index == len(a):
        print str(sum)
        return
    else:
        sumUsingRecursion(sum)


sumUsingForLoop()
sumUsingWhileLoop()
sumUsingRecursion()
