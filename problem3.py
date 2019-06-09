# add new array in between old array's above last element

a = [2, 1, 3, 3, 4, 4]
b = [6, 8, 9, 9, 9, 0, 7]
b.append(a[-1])

a.pop()

for x in b:
    a.append(x)

print(a)
