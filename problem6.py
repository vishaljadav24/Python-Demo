# Write a program that asks the user for a number n
# Let user choose to prints the sum or multiple of the numbers 1 to n

n = int(input("Enter the number == "))
num = 0

def solveProblem():
    choosen = int(
    input("Enter 1 for sum or 2 for multiple of 1 to entered number "))
    global num
    if choosen == 1:
        for x in range(1, n+1):
            num += x
    elif choosen == 2:
        num = 1
        for x in range(1, n+1):
            num *= x
    else:
        print "Please enter valid number"
        solveProblem()
        return

solveProblem()

print "total sum is " + str(num)
