numbers = [4, 5, 3, 7, 8, 2, 1, 6]
cnt = 0
for n in numbers:
    if n%2 == 0:
        cnt = cnt + 1
print("Počet =", cnt)