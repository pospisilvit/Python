numbers = [4, 8, 42, 77, 9, 5, 1]
max1 = 0
max2 = 0
for n in numbers:
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n
print(max2)
