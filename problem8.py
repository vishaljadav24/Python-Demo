# Write a function that returns the elements on odd positions in a list.

a = [32, 4, 46, 35, 3, 6, 54, 68, 2, 45, 65]

for index, x in enumerate(a, start=0):
    if index % 2 != 0:
        print x
